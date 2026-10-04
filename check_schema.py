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
    rows = cursor.fetchall()
    print("Table: assessments")
    for row in rows:
        print(row)
    
    cursor.execute("DESCRIBE users")
    rows = cursor.fetchall()
    print("\nTable: users")
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")
