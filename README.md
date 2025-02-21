# 📄 AI PDF Q&A System  

This is an AI-powered application that allows users to:  
✅ Upload a PDF and extract text  
✅ Store text embeddings in **MySQL** database  
✅ Ask questions and get relevant answers  

---

## 🚀 Technologies Used  
- **LangChain** for NLP processing  
- **Hugging Face Embeddings** for vectorization  
- **MySQL** for database storage  
- **Streamlit** for the UI  

---

## 🛠 Setup Instructions  

### 1️⃣ Clone the Repository  

_➤ git clone https://github.com/ankur2509/AI_PDF_QA.git_
_➤ cd AI_PDF_QA_

### 2️⃣ Install Dependencies
_➤ pip install -r requirements.txt_

### 3️⃣ Set Up MySQL Database
➤ Open MySQL and create a database + table:

_CREATE DATABASE ai_db;
USE ai_db;
CREATE TABLE embeddings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text TEXT,
    embedding TEXT
    );_

### 4️⃣ Run the Application
_➤ streamlit run pdf_app.py_

##📌 Features

✅ Upload and process PDF files
✅ Store extracted text embeddings in MySQL
✅ Retrieve the most relevant answers using vector search

