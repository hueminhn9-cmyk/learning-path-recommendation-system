import mysql.connector

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
    print(f"Assessments columns: {', '.join(cols)}")
    
    cursor.execute("DESCRIBE users")
    cols = [col[0] for col in cursor.fetchall()]
    print(f"Users columns: {', '.join(cols)}")

    cursor.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")
