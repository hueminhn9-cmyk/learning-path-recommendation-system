import mysql.connector

def check_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="student_learning_db"
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM courses")
        rows = cursor.fetchall()
        with open("db_dump.txt", "w") as f:
            for row in rows:
                f.write(f"ID: {row['id']}, Level: {row['level']}, Title: {row['title']}, URL: {row['url']}\n")
        cursor.close()
        conn.close()
    except Exception as e:
        with open("db_dump.txt", "w") as f:
            f.write(f"Error: {e}")

if __name__ == "__main__":
    check_db()
