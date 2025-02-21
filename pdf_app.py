import streamlit as st
import mysql.connector
import PyPDF2
import ast
from scipy.spatial.distance import cosine
from langchain_huggingface import HuggingFaceEmbeddings

# Function to connect to the database
def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anshu@123",
        database="ai_db"
    )
    return conn

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

# Load the embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Streamlit UI for uploading a PDF
st.title("AI-Powered PDF Q&A System")
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    # Extract text from the uploaded PDF
    extracted_text = extract_text_from_pdf(uploaded_file)
    
    # Generate embeddings for the extracted text
    embeddings = embedding_model.embed_documents([extracted_text])[0]

    # Store the text and its embedding in the database
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO embeddings (text, embedding) VALUES (%s, %s)", (extracted_text, str(embeddings)))
    conn.commit()
    conn.close()

    st.success("PDF processed and stored successfully!")

# Streamlit UI for asking a question
question = st.text_input("Ask a question about the PDF:")

if question:
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT text, embedding FROM embeddings")
    data = cursor.fetchall()
    conn.close()

    if not data:
        st.write("No documents found in the database.")
    else:
        stored_texts = []
        stored_embeddings = []

        # Retrieve stored text and embeddings from the database
        for row in data:
            stored_texts.append(row[0])
            stored_embeddings.append(ast.literal_eval(row[1]))  # Convert string back to a list

        # Generate embedding for the question
        question_embedding = embedding_model.embed_documents([question])[0]

        # Find the best matching stored text using cosine similarity
        best_match_index = 0
        best_similarity = float("inf")

        for i in range(len(stored_embeddings)):
            similarity = cosine(question_embedding, stored_embeddings[i])
            if similarity < best_similarity:
                best_similarity = similarity
                best_match_index = i

        best_answer = stored_texts[best_match_index]
        st.write(f"Answer: {best_answer}")
