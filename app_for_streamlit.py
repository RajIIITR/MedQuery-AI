import streamlit as st
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

# Load environment variables
load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Page configuration with custom theme
st.set_page_config(
    page_title="HealthBot - Your Medical Assistant",
    page_icon="🩺",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2c3e50;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #7f8c8d;
        font-weight: 400;
        margin-bottom: 2rem;
    }
    .stTextInput>div>div>input {
        border-radius: 20px;
    }
    .chat-container {
        border-radius: 10px;
        background-color: #f8f9fa;
        padding: 20px;
        margin-bottom: 20px;
        min-height: 300px;
        max-height: 500px;
        overflow-y: auto;
    }
    .user-message {
        background-color: #e3f2fd;
        border-radius: 15px 15px 3px 15px;
        padding: 10px 15px;
        margin-bottom: 10px;
        display: inline-block;
        max-width: 80%;
        float: right;
        clear: both;
    }
    .assistant-message {
        background-color: #f1f3f4;
        border-radius: 15px 15px 15px 3px;
        padding: 10px 15px;
        margin-bottom: 10px;
        display: inline-block;
        max-width: 80%;
        float: left;
        clear: both;
    }
    .footer {
        font-size: 0.8rem;
        color: #95a5a6;
        text-align: center;
        margin-top: 2rem;
    }
    .example-question {
        background-color: #f0f4f8;
        border-left: 3px solid #2e86de;
        padding: 8px 12px;
        margin-bottom: 8px;
        border-radius: 4px;
        font-size: 0.9rem;
    }
    .message-container {
        display: flex;
        flex-direction: column;
        width: 100%;
    }
    .message-wrapper {
        width: 100%;
        display: flex;
        margin-bottom: 10px;
        clear: both;
    }
    .user-wrapper {
        justify-content: flex-end;
    }
    .assistant-wrapper {
        justify-content: flex-start;
    }
</style>
""", unsafe_allow_html=True)

# Layout: Create two columns
col1, col2 = st.columns([2, 1])

with col1:
    # Main application area
    st.markdown('<div class="main-header">MedQuery AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Your AI Medical Assistant</div>', unsafe_allow_html=True)

    # Initialize session state for chat history if it doesn't exist
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Function to initialize the RAG pipeline
    @st.cache_resource
    def initialize_rag_pipeline():
        # Download embeddings
        embeddings = download_hugging_face_embeddings()
        
        index_name = "MedQuery AI"
        
        # Connect to existing Pinecone index
        docsearch = PineconeVectorStore.from_existing_index(
            index_name=index_name,
            embedding=embeddings
        )
        
        retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})
        
        # Initialize LLM
        llm = GoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0.4,
            max_tokens=500
        )
        
        # Create prompt template
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )
        
        # Create question-answer chain
        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        
        # Create retrieval chain
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)
        
        return rag_chain

    # Initialize the RAG pipeline
    rag_chain = initialize_rag_pipeline()

    # Chat container with better message display
    chat_container = st.container()
    with chat_container:
        st.markdown('<div class="message-container">', unsafe_allow_html=True)
        
        # Display chat history with improved styling
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f'<div class="message-wrapper user-wrapper"><div class="user-message">{message["content"]}</div></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="message-wrapper assistant-wrapper"><div class="assistant-message">{message["content"]}</div></div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Handle form submission to process both Enter key and button click
    with st.form(key="message_form", clear_on_submit=True):
        user_input = st.text_input(
            "Type your medical question here:",
            key="user_input",
            placeholder="What would you like to know about your health?",
        )
        submit_button = st.form_submit_button("Send")
        
    # Process user input
    if submit_button and user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Display thinking spinner
        with st.spinner("HealthBot is thinking..."):
            try:
                # Get response from RAG chain
                response = rag_chain.invoke({"input": user_input})
                answer = response["answer"]
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                error_message = f"Sorry, I encountered an error: {str(e)}"
                st.session_state.messages.append({"role": "assistant", "content": error_message})
        
        # Rerun the app to display the new messages
        st.rerun()

    # Footer
    st.markdown('<div class="footer">Powered by Google Gemini 2.0 Flash and Pinecone</div>', unsafe_allow_html=True)

with col2:
    # Sidebar content
    st.markdown("### About HealthBot")
    
    st.markdown("""
    HealthBot is an AI-powered medical assistant that uses advanced technology to provide reliable medical information.
    
    **Key Features:**
    
    ✅ **Retrieval-Augmented Generation** technology for accurate responses
    
    ✅ **Trusted Medical Sources** for reliable information
    
    ✅ **Conversational Interface** for natural interactions
    
    ✅ **Contextual Awareness** throughout your conversation
    """)
    
    st.markdown("---")
    
    st.markdown("### Important Disclaimer")
    
    st.warning("""
    This chatbot provides general information only and is not a substitute for professional medical advice, diagnosis, or treatment.
    
    Always consult with a qualified healthcare provider for medical concerns.
    """)
    
    st.markdown("---")
    
    # Add example questions as reference (not clickable buttons)
    st.markdown("### Example Questions")
    
    example_questions = [
        "What are the symptoms of diabetes?",
        "How can I manage high blood pressure?",
        "What causes migraines?",
        "Is it safe to exercise with asthma?",
        "What are the side effects of ibuprofen?"
    ]
    
    for question in example_questions:
        st.markdown(f'<div class="example-question">{question}</div>', unsafe_allow_html=True)