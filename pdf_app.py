import streamlit as st
import pymysql
import PyPDF2
import ast  # To convert stored string embeddings back to list
import scipy
from scipy.spatial.distance import cosine  # For similarity search

# NEW Imports (Updated)
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# venv\Scripts\activate #for virtual env.
# streamlit run pdf_app.py #for running it locally


# Database connection
def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Anshu@123",
        database="ai_db"
    )

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = "".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

# Initialize embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Streamlit UI
st.title("AI-Powered PDF Q&A System")
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    extracted_text = extract_text_from_pdf(uploaded_file)
    embeddings = embedding_model.embed_documents([extracted_text])[0]  # Generate embedding
    
    # Store embeddings in DB
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO embeddings (text, embedding) VALUES (%s, %s)", (extracted_text, str(embeddings)))
    conn.commit()
    conn.close()
    
    st.success("PDF processed and stored successfully!")

# Question answering
question = st.text_input("Ask a question about the PDF:")

if question:
    # Connect to DB and retrieve stored embeddings
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT text, embedding FROM embeddings")  # FIX: Now using the `embeddings` table
    documents = cursor.fetchall()
    conn.close()

    if not documents:
        st.write("No documents found in the database.")
    else:
        # Extract stored text and embeddings
        stored_texts = [doc[0] for doc in documents]
        stored_embeddings = [ast.literal_eval(doc[1]) for doc in documents]  # Convert string to list

        # Compute embedding for the question
        question_embedding = embedding_model.embed_documents([question])[0]

        # Find the most relevant text using cosine similarity
        best_match_idx = min(range(len(stored_embeddings)), key=lambda i: cosine(question_embedding, stored_embeddings[i]))
        best_answer = stored_texts[best_match_idx]

        st.write(f"Answer: {best_answer}")
