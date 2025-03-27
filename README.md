# 🩺 MedQuery AI: Advanced Medical Knowledge Assistant

## 🌟 Overview

MedQuery AI is an intelligent medical assistant powered by Retrieval-Augmented Generation (RAG). It leverages cutting-edge AI technologies including Google's Gemini AI, Hugging Face embeddings, and Pinecone vector database to provide accurate and contextual medical insights based on a stored medical book.

## 🚀 Features

- **📝 Text-Based Medical Queries**
  - Retrieves accurate medical insights from a pre-processed medical book
  - No external web search—responses strictly based on stored book content
  - Uses Pinecone vector database for fast and efficient search

- **📖 Multi-Modal Knowledge Base**
  - Book chunks embedded using Hugging Face Sentence Transformers
  - Cosine similarity search in Pinecone ensures most relevant results
  - Processed chunks enhanced by LLMs (Gemini-2.0-Flash or Azure GPT-3.5-Turbo)

## 🔄 Workflow

1. **Data Preparation & Embedding Storage**
   - Medical book split into chunks for efficient retrieval
   - Chunks converted to embeddings using pretrained model
   - Embeddings stored in Pinecone vector database

2. **Query Processing & Similarity Search**
   - User submits medical query
   - Query converted to embedding
   - Cosine similarity search retrieves top 3-5 most relevant book chunks

3. **Response Generation via RAG Pipeline**
   - Retrieved book chunks combined with user query
   - LLM generates comprehensive response

4. **Output Presentation**
   - AI-generated response displayed
   - Referenced book sections provided

## 🛠️ Installation

### Local Setup

1. Clone the Repository
```bash
git clone https://github.com/RajIIITR/medical-knowledge-assistant.git
cd medical-knowledge-assistant
```

2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Set Up Environment Variables
Create a `.env` file in the project root:
```ini
PINECONE_API_KEY=your_pinecone_key
GOOGLE_GENAI_KEY=your_google_ai_key
```

## 📌 Requirements

- Python 3.10
- Key Dependencies:
  - sentence-transformers==2.2.2
  - langchain==0.3.1
  - streamlit==1.29.0
  - (Full list in requirements.txt)

## ▶️ Usage

Run the Streamlit Application:
```bash
streamlit run app.py
```

### Interaction Modes
- **Text Query Mode**: Enter medical-related queries
- **Retrieval-Augmented Generation**: Fetches most relevant book chunks to generate informed responses

## 🌍 Deployment Options

- Streamlit Cloud
- AWS (EC2, Lambda, S3)
- Google Cloud Run

🔗 **Live Demo**: [https://medqueryai.streamlit.app/](https://medquery-ai.streamlit.app/)

## 📄 Project Structure
```
MedQueryAI/
├── app.py                 # Main Streamlit application
├── src/
│   ├── helper.py          # Helper functions for embeddings & retrieval
│   ├── prompt.py          # Query prompt templates
├── store_index.py         # Script to store book data in Pinecone
├── requirements.txt       # Dependencies
└── .env                   # API keys (ignored in Git)
```

## ⚠️ Disclaimer

🚨 **Important Medical Notice**: 
MedQuery AI provides informational support only. It does not replace professional medical advice. Always consult a healthcare professional for medical concerns.

## 💡 Future Improvements

- Integrate Real-Time Web Search
- Support Multi-Modal Queries with Medical Image Analysis
- Enhance Retrieval Efficiency with Hybrid Search

⭐ **Star this repository** if you find it useful!

## 🚀 Let’s revolutionize AI-powered medical assistance together! 🚀
