# Pravaah DL Hackathon - Grounded Causal Reasoning System

## Project Overview
This project implements a grounded causal reasoning system for the Pravaah DL Hackathon. The system uses advanced NLP techniques, sentence transformers, and FAISS indexing to perform causal analysis on conversational data.

## Web Application UI

The project includes a modern, responsive web interface with:

### Features:
- **Modern Design**: Beautiful gradient backgrounds with glassmorphism effects
- **Responsive Layout**: Works seamlessly on desktop and mobile devices
- **Interactive Elements**: Smooth animations and hover effects
- **Real-time Analysis**: Live query processing with loading indicators
- **Visual Statistics**: Dashboard-style metrics display
- **Conversation History**: Track all your queries in one place
- **Font Awesome Icons**: Professional iconography throughout

### Running the Web App:
```bash
# Start the Flask server
python app.py

# Or use the batch file (Windows)
start_webapp.bat

# Open browser to:
http://localhost:5000
```

## Repository Structure
```
.
├── PRAVAH_HACKTHON (1).ipynb          # Main notebook with complete implementation
├── InitialEDA.ipynb                    # Exploratory Data Analysis notebook
├── Grounded_Causal_Reasoning_Submission.csv  # Final submission file
├── Technical Report.docx               # Detailed technical documentation
├── requirement.txt                     # Python dependencies
├── df_turns_resampled.pkl             # Preprocessed data file
├── causal_engine_index.faiss          # FAISS index for similarity search
└── sentence_transformer_model.zip     # Pre-trained sentence transformer model
```

## Prerequisites
- Python 3.12+
- CUDA-compatible GPU (optional, for faster processing)
- Minimum 8GB RAM
- 10GB free disk space

## Environment Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/M0h1tkumar/Pravaah-Dl-hackthon.git
cd Pravaah-Dl-hackthon
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirement.txt
```

**Note:** The requirements file contains all necessary packages including:
- `transformers` - For transformer models
- `sentence-transformers` - For sentence embeddings
- `faiss-cpu` - For efficient similarity search
- `torch` - PyTorch framework
- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `scikit-learn` - Machine learning utilities

## Data Preprocessing

### Step 1: Extract Model Files
```bash
# Extract the sentence transformer model
unzip sentence_transformer_model.zip
```

### Step 2: Load Preprocessed Data
The preprocessed data is available in `df_turns_resampled.pkl`. This file contains:
- Resampled conversation turns
- Cleaned and tokenized text
- Feature engineered columns

## Running the System

### Option 1: Using Jupyter Notebook (Recommended)
```bash
# Start Jupyter Notebook
jupyter notebook

# Open PRAVAH_HACKTHON (1).ipynb
# Run all cells sequentially
```

### Option 2: Using Google Colab
1. Upload the notebook to Google Colab
2. Upload required data files (`df_turns_resampled.pkl`, `causal_engine_index.faiss`)
3. Install dependencies in the first cell
4. Run all cells

## Model Training

The system uses the following components:

### 1. Sentence Transformer Model
- **Model:** Pre-trained sentence transformer for semantic embeddings
- **Purpose:** Convert text to dense vector representations
- **Location:** `sentence_transformer_model.zip`

### 2. FAISS Index
- **Purpose:** Fast similarity search for causal reasoning
- **Index Type:** Flat L2 index
- **Location:** `causal_engine_index.faiss`

### Training Steps (if retraining is needed):
```python
# Load the notebook and execute the training cells
# The notebook contains:
# 1. Data loading and preprocessing
# 2. Model initialization
# 3. Embedding generation
# 4. FAISS index creation
# 5. Model evaluation
```

## Execution Workflow

### Step 1: Data Loading
```python
import pandas as pd
import pickle

# Load preprocessed data
with open('df_turns_resampled.pkl', 'rb') as f:
    df = pickle.load(f)
```

### Step 2: Load Models
```python
from sentence_transformers import SentenceTransformer
import faiss

# Load sentence transformer
model = SentenceTransformer('./sentence_transformer_model')

# Load FAISS index
index = faiss.read_index('causal_engine_index.faiss')
```

### Step 3: Run Inference
```python
# The notebook contains complete inference pipeline
# Execute cells in sequence for:
# - Query processing
# - Embedding generation
# - Similarity search
# - Causal reasoning
# - Result generation
```

### Step 4: Generate Submission
```python
# Final predictions are saved to:
# Grounded_Causal_Reasoning_Submission.csv
```

## Key Features

1. **Semantic Search:** Uses sentence transformers for semantic understanding
2. **Efficient Retrieval:** FAISS indexing for fast similarity search
3. **Causal Analysis:** Identifies causal relationships in conversations
4. **Scalable:** Handles large datasets efficiently

## Output

The system generates:
- `Grounded_Causal_Reasoning_Submission.csv` - Final predictions with causal reasoning results
- Intermediate analysis files (if enabled in notebook)
- Performance metrics and evaluation results

## Performance Metrics

The model is evaluated on:
- Accuracy
- Precision
- Recall
- F1-Score
- Inference time

## Troubleshooting

### Common Issues:

1. **Memory Error:**
   - Reduce batch size in the notebook
   - Use CPU instead of GPU if memory is limited

2. **FAISS Import Error:**
   ```bash
   pip install faiss-cpu --force-reinstall
   ```

3. **Model Loading Error:**
   - Ensure `sentence_transformer_model.zip` is extracted
   - Check file paths in the notebook

4. **Pickle Loading Error:**
   - Ensure Python version compatibility
   - Regenerate pickle file if needed

## Additional Resources

- **Technical Report:** See `Technical Report.docx` for detailed methodology
- **EDA Notebook:** See `InitialEDA.ipynb` for data exploration
- **Main Implementation:** See `PRAVAH_HACKTHON (1).ipynb` for complete code

## System Requirements

### Minimum:
- CPU: 4 cores
- RAM: 8GB
- Storage: 10GB

### Recommended:
- CPU: 8+ cores
- RAM: 16GB+
- GPU: NVIDIA GPU with 6GB+ VRAM
- Storage: 20GB SSD

## Contact & Support

For issues or questions:
- Create an issue in the GitHub repository
- Contact: [Repository Owner]

## License

This project is submitted for the Pravaah DL Hackathon.

## Acknowledgments

- Pravaah DL Hackathon organizers
- Open-source libraries: Transformers, FAISS, Sentence-Transformers
- Pre-trained models from Hugging Face

---

**Note:** Ensure all data files are present before running the system. The notebook contains detailed comments and documentation for each step.
