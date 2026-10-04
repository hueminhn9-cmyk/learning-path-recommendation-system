import mysql.connector
from mysql.connector import Error

def check_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        if conn.is_connected():
            print("Successfully connected to MySQL server")
            conn.close()
        return True
    except Error as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    check_mysql()
