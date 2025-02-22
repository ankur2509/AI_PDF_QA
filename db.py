import pymysql

# Connect to MySQL
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Anshu@123",
    database="ai_db"
)
cur = conn.cursor()

# Test the connection
cur.execute("SHOW TABLES;")
tables = cur.fetchall()
print("✅ Connected to MySQL! Tables:", tables)

cur.close()
conn.close()
