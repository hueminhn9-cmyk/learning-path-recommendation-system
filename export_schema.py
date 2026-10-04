import mysql.connector
import json

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='student_learning_db'
    )
    cursor = conn.cursor()
    cursor.execute("DESCRIBE assessments")
    cols = [col[0] for col in cursor.fetchall()]
    with open('schema_debug.json', 'w') as f:
        json.dump(cols, f)
    conn.close()
except Exception as e:
    with open('schema_debug.json', 'w') as f:
        json.dump({"error": str(e)}, f)
