import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='student_learning_db'
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    print("Existing Users:")
    for row in rows:
        print(f"ID: {row['id']}, Email: {row['email']}, Password: {row['password']}")
    
    if not rows:
        print("No users found. Adding default student user.")
        cursor.execute("INSERT INTO users (email, password, name, roll_number, interest) VALUES (%s, %s, %s, %s, %s)", 
                       ("student@college.edu", "password123", "Default Student", "S101", "High"))
        conn.commit()
        print("Default student user 'student@college.edu' with password 'password123' added.")

    cursor.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")
