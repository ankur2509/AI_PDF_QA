import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="ai_db"
)
cur = conn.cursor()

# Test the connection
cur.execute("SHOW TABLES;")
tables = cur.fetchall()
print("✅ Connected to MySQL! Tables:", tables)

cur.close()
conn.close()
