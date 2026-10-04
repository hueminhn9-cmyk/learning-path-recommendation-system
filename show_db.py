import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='student_learning_db'
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
        SELECT u.name, u.roll_number, a.subject, a.marks, a.predicted_level 
        FROM assessments a 
        JOIN users u ON a.user_id = u.id
        ORDER BY a.created_at DESC
    ''')
    rows = cursor.fetchall()
    print("| Name | Roll | Subject | Marks | Level |")
    print("|---|---|---|---|---|")
    for row in rows:
        print(f"| {row['name']} | {row['roll_number']} | {row['subject']} | {row['marks']}% | {row['predicted_level']} |")
    
    cursor.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")
