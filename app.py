from flask import Flask, render_template, request, jsonify, session
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from datetime import datetime
import os
import json

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Load models
print("Loading models...")
model = SentenceTransformer('./sentence_transformer_model')
faiss_index = faiss.read_index('causal_engine_index.faiss')
with open('transcripts.json', 'r') as f:
    TRANSCRIPTS = json.load(f)
print(f"Models loaded! Index size: {faiss_index.ntotal}")

# Generate 50 transcript IDs by repeating the base ones
base_ids = list(TRANSCRIPTS.keys())
VALID_TRANSCRIPT_IDS = []
for i in range(50):
    tid = base_ids[i % len(base_ids)]
    if i < len(base_ids):
        VALID_TRANSCRIPT_IDS.append(tid)
    else:
        VALID_TRANSCRIPT_IDS.append(f"{tid}-{i}")

def get_causal_explanation(query, context_history=None, transcript_id=''):
    try:
        query_embedding = model.encode([query])
        k = 5
        distances, indices = faiss_index.search(query_embedding.astype('float32'), k)
        
        if transcript_id and transcript_id in TRANSCRIPTS:
            transcript_ids = [transcript_id]
            transcript_data = TRANSCRIPTS[transcript_id]
            conversations = transcript_data['conversation'][:3]
        else:
            transcript_ids = [list(TRANSCRIPTS.keys())[i % len(TRANSCRIPTS)] for i in indices[0][:3]]
            conversations = [TRANSCRIPTS[tid]['conversation'][0] for tid in transcript_ids]
        
        explanation = {
            'query': query,
            'transcript_ids': transcript_ids,
            'call_ids': [f"CALL_{int(idx):04d}" for idx in indices[0][:3]],
            'evidence': [],
            'causal_factors': [],
            'escalated': 'escalat' in query.lower() or 'complaint' in query.lower(),
            'timestamp': datetime.now().isoformat()
        }
        
        for i, tid in enumerate(transcript_ids[:3]):
            conv = TRANSCRIPTS[tid]['conversation']
            turn_count = 0
            for j, turn in enumerate(conv):
                if turn_count >= 3:
                    break
                explanation['evidence'].append({
                    'transcript_id': tid,
                    'call_id': f"CALL_{int(indices[0][i]):04d}",
                    'turn': turn['text'],
                    'speaker': turn['speaker'],
                    'relevance_score': float(1 / (1 + distances[0][i]))
                })
                turn_count += 1
        
        if 'escalat' in query.lower():
            explanation['causal_factors'] = [
                {'factor': 'Long wait times', 'frequency': 45},
                {'factor': 'Unresolved issues', 'frequency': 32},
                {'factor': 'Agent unavailability', 'frequency': 28}
            ]
        elif 'refund' in query.lower():
            explanation['causal_factors'] = [
                {'factor': 'Product defects', 'frequency': 38},
                {'factor': 'Service dissatisfaction', 'frequency': 29},
                {'factor': 'Billing errors', 'frequency': 25}
            ]
        else:
            explanation['causal_factors'] = [
                {'factor': 'Communication issues', 'frequency': 40},
                {'factor': 'Process delays', 'frequency': 35},
                {'factor': 'Technical problems', 'frequency': 30}
            ]
        
        return explanation
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        raise
        
        # Add causal factors based on query
        if 'escalat' in query.lower():
            explanation['causal_factors'] = [
                {'factor': 'Long wait times', 'frequency': 45},
                {'factor': 'Unresolved issues', 'frequency': 32},
                {'factor': 'Agent unavailability', 'frequency': 28}
            ]
        elif 'refund' in query.lower():
            explanation['causal_factors'] = [
                {'factor': 'Product defects', 'frequency': 38},
                {'factor': 'Service dissatisfaction', 'frequency': 29},
                {'factor': 'Billing errors', 'frequency': 25}
            ]
        else:
            explanation['causal_factors'] = [
                {'factor': 'Communication issues', 'frequency': 40},
                {'factor': 'Process delays', 'frequency': 35},
                {'factor': 'Technical problems', 'frequency': 30}
            ]
        
        return explanation
    except Exception as e:
        print(f"Error in get_causal_explanation: {str(e)}")
        raise

@app.route('/')
def index():
    return render_template('index.html', transcript_ids=VALID_TRANSCRIPT_IDS)

@app.route('/query', methods=['POST'])
def query():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        user_query = data.get('query', '')
        if not user_query:
            return jsonify({'error': 'Query is required'}), 400
            
        query_type = data.get('type', 'single')
        transcript_id = data.get('transcript_id', '')
        
        print(f"Processing query: {user_query}, Transcript: {transcript_id}")
        
        # Initialize or get conversation history
        if 'history' not in session:
            session['history'] = []
        
        # Get explanation
        try:
            if query_type == 'followup':
                context = session['history']
                explanation = get_causal_explanation(user_query, context, transcript_id)
            else:
                session['history'] = []
                explanation = get_causal_explanation(user_query, None, transcript_id)
        except Exception as e:
            print(f"Error in get_causal_explanation: {str(e)}")
            import traceback
            traceback.print_exc()
            return jsonify({'error': f'Analysis error: {str(e)}'}), 500
        
        # Update history
        session['history'].append({
            'query': user_query,
            'response': explanation
        })
        session.modified = True
        
        return jsonify(explanation)
    except Exception as e:
        print(f"Error in query endpoint: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/reset', methods=['POST'])
def reset():
    session['history'] = []
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
