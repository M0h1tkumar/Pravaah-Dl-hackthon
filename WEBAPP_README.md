# Grounded Causal Reasoning Web Application

## Quick Start

### 1. Install Dependencies
```bash
pip install flask sentence-transformers faiss-cpu pandas numpy
```

### 2. Extract Model Files
```bash
unzip sentence_transformer_model.zip
```

### 3. Run the Application
```bash
python app.py
```

### 4. Access the Web Interface
Open your browser and navigate to:
```
http://localhost:5000
```

## Features

### Single Query Mode
- Submit analytical queries about conversational outcomes
- Get causal explanations with evidence
- View relevant Call IDs and dialogue turns

### Follow-up Query Mode
- Ask context-aware follow-up questions
- System maintains conversation history
- Build upon previous analyses

### Key Capabilities
- **Evidence-Based Analysis**: All responses grounded in actual conversation data
- **Call ID Tracking**: Identifies specific conversations related to outcomes
- **Relevance Scoring**: Shows confidence in evidence retrieval
- **Causal Factor Identification**: Highlights patterns associated with events
- **Multi-Turn Context**: Maintains consistency across conversation

## Usage Examples

### Single Query
```
Query: "Why do customers escalate complaints after long wait times?"
```

### Follow-up Query
```
Initial: "What conversational patterns lead to refund requests?"
Follow-up: "Can you show me specific examples from those conversations?"
```

## Sample Queries
See `sample_queries.csv` for example queries covering:
- Escalation analysis
- Refund pattern identification
- Agent behavior assessment
- Temporal factor analysis
- Competitive mention impact

## Architecture

- **Backend**: Flask (Python)
- **Frontend**: Pure HTML/CSS/JavaScript
- **ML Models**: Sentence Transformers + FAISS
- **Data**: Preprocessed conversation transcripts

## API Endpoints

### POST /query
Submit analytical query
```json
{
  "query": "Your question here",
  "type": "single" | "followup"
}
```

### POST /reset
Reset conversation history

## Troubleshooting

**Model Loading Error**: Ensure `sentence_transformer_model.zip` is extracted
**FAISS Error**: Install `faiss-cpu` or `faiss-gpu`
**Port Conflict**: Change port in `app.py` (default: 5000)
