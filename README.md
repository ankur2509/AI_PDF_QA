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
_**git clone https://github.com/ankur2509/AI_PDF_QA.git**
**cd AI_PDF_QA**_

2️⃣ Install Dependencies
_**->pip install -r requirements.txt**_

3️⃣ Set Up MySQL Database

**_Open MySQL and create a database + table:_**
->sql

_**CREATE DATABASE ai_db;**_
_**USE ai_db;**_

_**CREATE TABLE embeddings (**_
  _ **id INT AUTO_INCREMENT PRIMARY KEY,**_
  _ **text TEXT,**_
  _  **embedding TEXT**_
_**);**_

->Update database credentials in pdf_app.py if needed:
#python

_**def connect_db():_
    _return mysql.connector.connect(_
       _ host="your_mysql_host",_
        _user="your_mysql_user",_
        _password="your_mysql_password",_
      _  database="ai_db"_
_    )**_
    
4️⃣ Run the Application
_**->streamlit run pdf_app.py**_

📌 Features
->Upload and process PDF files
->Store extracted text embeddings in MySQL
->Retrieve the most relevant answers using vector search




