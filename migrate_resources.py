import mysql.connector

# Hardcoded resources from flask_app.py
resources_list = [
    {"title": "Introduction to Data Science", "level": "Beginner", "type": "Video", "link": "https://www.youtube.com/watch?v=ua-CiDNNj30", "subject": "Data Science"},
    {"title": "Python for Data Analysis", "level": "Beginner", "type": "Course", "link": "https://www.coursera.org/learn/python-for-data-analysis", "subject": "Data Science"},
    {"title": "Machine Learning Basics", "level": "Intermediate", "type": "Video", "link": "https://www.youtube.com/watch?v=GwIo3gDZCVQ", "subject": "Machine Learning"},
    {"title": "Advanced Neural Networks", "level": "Advanced", "type": "Specialization", "link": "https://www.deeplearning.ai/program/deep-learning-specialization/", "subject": "Deep Learning"},
    {"title": "Big Data Engineering", "level": "Advanced", "type": "Book", "link": "https://www.oreilly.com/library/view/big-data/9781449327422/", "subject": "Big Data"},
    {"title": "Web Development Bootcamp", "level": "Beginner", "type": "Course", "link": "https://www.udemy.com/course/the-web-developer-bootcamp/", "subject": "Web Development"},
    {"title": "Cloud Computing Essentials", "level": "Intermediate", "type": "Video", "link": "https://www.youtube.com/watch?v=2LaAJq1lB1Q", "subject": "Cloud Computing"},
]

def migrate():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='student_learning_db'
        )
        cursor = conn.cursor()

        # Create table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resources (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                level VARCHAR(50) NOT NULL,
                type VARCHAR(50),
                link TEXT,
                subject VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Clear existing to avoid duplicates in this migration
        cursor.execute("DELETE FROM resources")

        # Insert data
        query = "INSERT INTO resources (title, level, type, link, subject) VALUES (%s, %s, %s, %s, %s)"
        for res in resources_list:
            cursor.execute(query, (res['title'], res['level'], res['type'], res['link'], res['subject']))
        
        conn.commit()
        print(f"Successfully migrated {len(resources_list)} resources to the database.")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Migration error: {e}")

if __name__ == "__main__":
    migrate()
