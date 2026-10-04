import mysql.connector

def fix_data():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='student_learning_db'
        )
        cursor = conn.cursor()
        
        # Clear existing courses
        cursor.execute("DELETE FROM courses")
        print("Cleared existing courses.")
        
        # New dummy data with fully unique URLs and proper titles for all levels
        courses_data = [
            # Data Science
            ("Beginner", "Introduction to Data Science & Analytics", "https://www.youtube.com/results?search_query=Data+Science+Beginner", "Core concepts of data manipulation and analysis.", "Data Science"),
            ("Intermediate", "Data Science: Exploratory Data Analysis", "https://www.youtube.com/results?search_query=Data+Science+Intermediate", "Deep dive into Pandas, Matplotlib, and EDA.", "Data Science"),
            ("Advanced", "Advanced Feature Engineering & Statistical Modeling", "https://www.youtube.com/results?search_query=Data+Science+Advanced", "Mastering predictive modeling and statistical inference.", "Data Science"),
            
            # Machine Learning
            ("Beginner", "Machine Learning Fundamentals", "https://www.youtube.com/results?search_query=Machine+Learning+Basics", "Introduction to supervised and unsupervised learning.", "Machine Learning"),
            ("Intermediate", "Machine Learning: Algorithms in Practice", "https://www.youtube.com/results?search_query=Machine+Learning+Intermediate", "Applying SVMs, Random Forests, and Gradient Boosting.", "Machine Learning"),
            ("Advanced", "Machine Learning System Design & MLOps", "https://www.youtube.com/results?search_query=MLOps+Advanced", "Deploying and scaling machine learning models in production.", "Machine Learning"),
            
            # Deep Learning
            ("Beginner", "Neural Networks for Beginners", "https://www.youtube.com/results?search_query=Neural+Networks+Beginner", "Understanding perceptrons and forward propagation.", "Deep Learning"),
            ("Intermediate", "Convolutional & Recurrent Neural Networks", "https://www.youtube.com/results?search_query=CNN+RNN+Tutorial", "Building image and text recognition models.", "Deep Learning"),
            ("Advanced", "Advanced Deep Learning: GANs & Transformers", "https://www.youtube.com/results?search_query=GANs+Transformers", "Cutting-edge deep learning architectures and attention mechanisms.", "Deep Learning"),
            
            # Big Data
            ("Beginner", "Big Data Concepts and Hadoop", "https://www.youtube.com/results?search_query=Big+Data+Hadoop", "Understanding distributed systems and Hadoop ecosystem.", "Big Data"),
            ("Intermediate", "Apache Spark & Data Processing", "https://www.youtube.com/results?search_query=Apache+Spark+Intermediate", "Fast data processing with Spark DataFrames.", "Big Data"),
            ("Advanced", "Real-Time Big Data Streaming Architecture", "https://www.youtube.com/results?search_query=Kafka+Spark+Streaming", "Building real-time data pipelines with Kafka and Spark Streaming.", "Big Data"),
            
            # Cloud Computing
            ("Beginner", "Cloud Computing Foundations", "https://www.youtube.com/results?search_query=Cloud+Computing+Basics", "Introduction to AWS, Azure, and GCP core services.", "Cloud Computing"),
            ("Intermediate", "Cloud Docker & Kubernetes Orchestration", "https://www.youtube.com/results?search_query=Docker+Kubernetes", "Container management and microservices deployment.", "Cloud Computing"),
            ("Advanced", "Advanced Cloud Solutions Architecture", "https://www.youtube.com/results?search_query=Advanced+Cloud+Architecture", "Designing highly available, scalable enterprise cloud systems.", "Cloud Computing"),
            
            # Web Development
            ("Beginner", "Modern Web Development Boot Camp", "https://www.youtube.com/results?search_query=Web+Development+HTML+CSS+JS", "Building foundational frontend skills.", "Web Development"),
            ("Intermediate", "Full-Stack React & Node.js", "https://www.youtube.com/results?search_query=React+NodeJS+Fullstack", "Building interactive web apps with React and Express.", "Web Development"),
            ("Advanced", "Web Development: Microservices & Performance", "https://www.youtube.com/results?search_query=Web+Microservices+Deployment", "Advanced backend architecture and high-performance rendering.", "Web Development"),
            
            # General
            ("Beginner", "Programming Foundations: Python", "https://www.youtube.com/results?search_query=Python+Programming+Beginner", "Essential logic and programming syntax.", "General"),
            ("Intermediate", "Data Structures & Algorithms in Python", "https://www.youtube.com/results?search_query=Python+Data+Structures", "Mastering key programming structures and efficiency.", "General"),
            ("Advanced", "Software Architecture & System Design", "https://www.youtube.com/results?search_query=System+Design+Interview", "Designing scalable applications from the ground up.", "General")
        ]
        
        query = "INSERT INTO courses (level, title, url, description, subject) VALUES (%s, %s, %s, %s, %s)"
        cursor.executemany(query, courses_data)
        
        conn.commit()
        print(f"Successfully inserted {len(courses_data)} subject-specific courses.")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fix_data()
