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
#bash
**git clone https://github.com/ankur2509/AI_PDF_QA.git**
**cd AI_PDF_QA**

2️⃣ Install Dependencies
**->pip install -r requirements.txt**

3️⃣ Set Up MySQL Database
Open MySQL and create a database + table:
->sql

**CREATE DATABASE ai_db;**
**USE ai_db;**

**CREATE TABLE embeddings (**
   **id INT AUTO_INCREMENT PRIMARY KEY,**
   **text TEXT,**
    **embedding TEXT**
**);**

->Update database credentials in pdf_app.py if needed:
#python

**def connect_db():
    return mysql.connector.connect(
        host="your_mysql_host",
        user="your_mysql_user",
        password="your_mysql_password",
        database="ai_db"
    )**
    
4️⃣ Run the Application
**->streamlit run pdf_app.py**

📌 Features
->Upload and process PDF files
->Store extracted text embeddings in MySQL
->Retrieve the most relevant answers using vector search




