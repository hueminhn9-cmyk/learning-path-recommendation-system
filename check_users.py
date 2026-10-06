import sqlite3

def check_users():
    conn = sqlite3.connect("student_learning_db.sqlite")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name, roll_number, email, password, role, interest, current_level FROM users")
    users = cursor.fetchall()
    
    print("\n================ DANH SACH NGUOI DUNG TRONG SQLITE ================")
    print(f"{'ID':<4} | {'Full Name':<20} | {'Email':<25} | {'Password':<10} | {'Role':<8}")
    print("-" * 75)
    for u in users:
        print(f"{u['id']:<4} | {u['name']:<20} | {u['email']:<25} | {u['password']:<10} | {u['role']:<8}")
    print("====================================================================\n")
    
    conn.close()

if __name__ == "__main__":
    check_users()


