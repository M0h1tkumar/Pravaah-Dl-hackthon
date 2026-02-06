# प्रभाव AI | ପ୍ରଭାବ AI | Prabhav AI

**Advanced Conversational Analytics Powered by AI**

A grounded causal reasoning system for analyzing conversational data and identifying causal factors behind outcome events. Built for the Pravaah DL Hackathon.

## 🌟 Features

- **Multilingual Interface**: Supports Hindi, Odia, and English
- **Modern Web UI**: Clean, professional design with dark theme
- **Real-time Analysis**: Fast query processing with FAISS indexing
- **Evidence-Based**: All responses grounded in actual conversation data
- **Causal Reasoning**: Identifies patterns and factors leading to outcomes
- **Interactive Dashboard**: Statistics and visual metrics
- **Conversation History**: Track all queries in one session

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- 8GB RAM minimum
- 10GB free disk space

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/prabhav-ai.git
cd prabhav-ai
```

2. **Create virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirement.txt
```

4. **Download model files**
Due to file size limitations, download these files separately:
- `sentence_transformer_model.zip` - [Download Link]
- `df_turns_resampled.pkl` - [Download Link]
- `causal_engine_index.faiss` - [Download Link]
- `transcripts.json` - [Download Link]

Extract the model:
```bash
unzip sentence_transformer_model.zip
```

5. **Run the application**
```bash
python app.py
```

6. **Open browser**
Navigate to: `http://localhost:5000`

## 📁 Project Structure

```
.
├── app.py                          # Flask web application
├── templates/
│   └── index.html                  # Web UI
├── sentence_transformer_model/     # Pre-trained model
├── causal_engine_index.faiss       # FAISS index
├── df_turns_resampled.pkl          # Preprocessed data
├── transcripts.json                # Conversation data
├── requirement.txt                 # Python dependencies
├── PRAVAH_HACKTHON (1).ipynb       # Main notebook
├── InitialEDA.ipynb                # Exploratory analysis
├── Technical Report.docx           # Documentation
└── README.md                       # This file
```

## 💻 Usage

### Web Interface

1. **Select Query Type**
   - Single Query: New analysis
   - Follow-up Query: Contextual continuation

2. **Choose Transcript** (Optional)
   - Select specific transcript or analyze all

3. **Enter Query**
   ```
   Example: "Why do customers escalate complaints?"
   ```

4. **View Results**
   - Query summary
   - Statistics dashboard
   - Relevant transcripts and calls
   - Evidence with relevance scores
   - Causal factors

### Jupyter Notebook

Open `PRAVAH_HACKTHON (1).ipynb` for:
- Complete implementation
- Model training
- Data preprocessing
- Evaluation metrics

## 🎯 Sample Queries

- "Why do customers escalate complaints after long wait times?"
- "What causes refund requests?"
- "Identify patterns in customer dissatisfaction"
- "What factors lead to call escalations?"
- "Analyze reasons for service complaints"

## 🛠️ Technology Stack

- **Backend**: Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **ML Framework**: PyTorch, Sentence Transformers
- **Search**: FAISS (Facebook AI Similarity Search)
- **Data Processing**: Pandas, NumPy
- **NLP**: Transformers, Sentence-BERT

## 📊 Model Architecture

1. **Sentence Transformer**: Converts text to semantic embeddings
2. **FAISS Index**: Fast similarity search for retrieval
3. **Causal Analysis**: Pattern identification and frequency analysis
4. **Evidence Grounding**: Links predictions to source conversations

## 🎨 UI Features

- **Dark Theme**: Professional slate gradient background
- **Cyan/Teal Accents**: Modern color scheme
- **Glassmorphism**: Frosted glass effect panels
- **Responsive Design**: Works on desktop and mobile
- **Smooth Animations**: Enhanced user experience
- **Clean Interface**: No clutter, text-focused design

## 📈 Performance

- **Query Time**: 2-5 seconds average
- **Accuracy**: High relevance scoring
- **Scalability**: Handles large conversation datasets
- **Efficiency**: Optimized FAISS indexing

## 🔧 Configuration

Edit `app.py` to customize:
- Port number (default: 5000)
- Model paths
- FAISS index parameters
- Session settings

## 📝 API Endpoints

### POST /query
Submit analytical query
```json
{
  "query": "Your question",
  "type": "single",
  "transcript_id": "optional"
}
```

### POST /reset
Reset conversation history

## 🐛 Troubleshooting

**Issue**: Model not loading
**Solution**: Ensure `sentence_transformer_model.zip` is extracted

**Issue**: FAISS import error
**Solution**: `pip install faiss-cpu --force-reinstall`

**Issue**: Port already in use
**Solution**: Change port in `app.py` or kill process on port 5000

**Issue**: Memory error
**Solution**: Reduce batch size or use smaller dataset

## 📄 License

This project was created for the Pravaah DL Hackathon.

## 🙏 Acknowledgments

- Pravaah DL Hackathon organizers
- Hugging Face for pre-trained models
- FAISS team at Facebook AI Research
- Open-source community

## 👥 Contributors

- [Your Name]
- [Team Members]

## 📧 Contact

For questions or issues:
- Create an issue in this repository
- Email: [your-email@example.com]

## 🌐 Links

- [Technical Report](Technical%20Report.docx)
- [Demo Video](#)
- [Presentation](#)

---

**Made with ❤️ for Pravaah DL Hackathon**
