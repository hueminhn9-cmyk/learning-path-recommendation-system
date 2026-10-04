import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='student_learning_db'
    )
    cursor = conn.cursor(dictionary=True)
    
    email = "student@college.edu"
    password = "password123"
    
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    if not cursor.fetchone():
        print(f"Adding {email}...")
        cursor.execute("INSERT INTO users (email, password, name, roll_number, interest) VALUES (%s, %s, %s, %s, %s)", 
                       (email, password, "Default Student", "S101", "High"))
        conn.commit()
        print(f"User {email} added with password {password}.")
    else:
        print(f"User {email} already exists.")

    cursor.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")
