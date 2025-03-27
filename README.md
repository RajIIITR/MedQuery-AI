🩺 MedQuery AI: Advanced Medical Knowledge Assistant
🌟 Overview
MedQuery AI is an intelligent medical assistant powered by Retrieval-Augmented Generation (RAG). It utilizes Google's Gemini AI, Hugging Face embeddings, and Pinecone vector database to provide accurate and contextual medical insights based on a stored medical book.

This AI-powered system processes text-based queries by retrieving relevant medical knowledge from a pre-indexed book and enhances responses using a large language model (LLM).

🚀 Features
📝 Text-Based Medical Queries
Retrieves accurate medical insights from a pre-processed medical book.

No external web search—all responses are based strictly on the stored book content.

Uses Pinecone vector database for fast and efficient search.

📖 Multi-Modal Knowledge Base
Book chunks are embedded using Hugging Face Sentence Transformers.

Cosine similarity search in Pinecone ensures the most relevant results.

Processed chunks are passed to LLMs (Gemini-2.0-Flash or Azure GPT-3.5-Turbo) for enhanced answer generation.

🔄 Workflow
1️⃣ Data Preparation & Embedding Storage
A medical book is split into chunks for efficient retrieval.

Each chunk is converted into embeddings using a pretrained embedding model.

The chunk embeddings are stored in Pinecone vector database for similarity-based search.

2️⃣ Query Processing & Similarity Search
The user submits a query related to medical topics.

The query is converted into an embedding using the same embedding model.

A cosine similarity search is performed in Pinecone, retrieving the top 3-5 most relevant book chunks.

3️⃣ Response Generation via LLM (RAG Pipeline)
The retrieved book chunks are combined with the user query.

The LLM (Gemini-2.0-Flash or GPT-3.5-Turbo) processes this input and generates a response.

4️⃣ Output Presentation
The AI-generated response is displayed along with referenced book sections.

The system provides reliable, book-based medical information.

🛠️ Installation
Local Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/RajIIITR/medical-knowledge-assistant.git
cd medical-knowledge-assistant
2️⃣ Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up Environment Variables
Create a .env file in the project root and add the necessary API keys:

ini
Copy
Edit
PINECONE_API_KEY=your_pinecone_key
GOOGLE_GENAI_KEY=your_google_ai_key
📌 Requirements
Python 3.10

Key Dependencies:

txt
Copy
Edit
sentence-transformers==2.2.2
langchain==0.3.1
pypdf==3.12.0
python-dotenv==1.0.1
langchain-pinecone==0.2.3
langchain-community==0.3.1
langchain-experimental==0.0.1
langchain-google-genai==2.0.11
duckduckgo-search==7.5.3
torch==2.6.0
torchaudio==2.6.0
torchvision==0.21.0
streamlit==1.29.0
▶️ Usage
Run the Streamlit Application
bash
Copy
Edit
streamlit run app.py
Using MedQuery AI
Text Query Mode:

Enter a medical-related query.

The AI retrieves relevant book-based information and generates an answer.

Retrieval-Augmented Generation (RAG):

The system fetches the most relevant book chunks based on the user query.

These are passed to LLM to generate a well-informed response.

🌍 Deployment
Streamlit App
🔗 Live Demo: https://medqueryai.streamlit.app/

Deployment Options
Streamlit Cloud

AWS (EC2, Lambda, S3)

Google Cloud Run

📄 Project Structure
bash
Copy
Edit
MedQueryAI/
├── app.py                 # Main Streamlit application
├── src/
│   ├── helper.py          # Helper functions for embeddings & retrieval
│   ├── prompt.py          # Query prompt templates
├── store_index.py         # Script to store book data in Pinecone
├── requirements.txt       # Dependencies
└── .env                   # API keys (ignored in Git)
⚠️ Disclaimer
🚨 Important Medical Notice:
MedQuery AI provides informational support only. It does not replace professional medical advice. Always consult a healthcare professional for medical concerns.

💡 Future Improvements
🔹 Integrate Real-Time Web Search – Fetch real-time medical data from DuckDuckGo or Google.
🔹 Expand to Multi-Modal Queries – Support medical image analysis using AI-powered vision models.
🔹 Enhance Retrieval Efficiency – Experiment with Hybrid Search (Dense + Keyword Search).
