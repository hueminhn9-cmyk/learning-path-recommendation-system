import sqlite3

DB_PATH = "student_learning_db.sqlite"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_sqlite_db():
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            roll_number TEXT,
            interest TEXT DEFAULT 'Medium',
            current_level TEXT DEFAULT 'Beginner',
            role TEXT DEFAULT 'student'
        )
    ''')
    
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO users (email, password, name, roll_number, interest, role) VALUES (?, ?, ?, ?, ?, ?)",
                       ("student@college.edu", "123456", "Tran Van A", "SV001", "High", "student"))
        cursor.execute("INSERT INTO users (email, password, name, roll_number, interest, role) VALUES (?, ?, ?, ?, ?, ?)",
                       ("admin@college.edu", "admin123", "System Administrator", "ADM001", "High", "admin"))
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS assessments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            student_name TEXT,
            subject TEXT,
            marks INTEGER,
            interest TEXT,
            time_spent REAL,
            predicted_level TEXT,
            confidence REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT,
            level TEXT,
            title TEXT,
            url TEXT,
            description TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            subject TEXT,
            goal_title TEXT,
            target_date TEXT,
            status TEXT DEFAULT 'In Progress',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    
    cursor.execute("SELECT COUNT(*) FROM courses")
    if cursor.fetchone()[0] == 0:
        courses_seed = [
            ("Machine Learning", "Beginner", "Machine Learning Basics for Beginners", "https://www.youtube.com/watch?v=GwIo3gDZCVQ", "Supervised learning: Linear Regression, Logistic Regression, KNN."),
            ("Machine Learning", "Beginner", "Scikit-Learn Crash Course", "https://www.youtube.com/watch?v=pqNCD_5r0IU", "Build classification and regression models step-by-step."),
            ("Machine Learning", "Intermediate", "ML Algorithms & Evaluation Metrics", "https://www.youtube.com/watch?v=Gv9_4yMHFhI", "Decision Trees, Random Forests, cross-validation, and hyperparameter tuning."),
            ("Machine Learning", "Intermediate", "Hands-On ML Code Projects", "https://github.com/ageron/handson-ml3", "End-to-end Machine Learning project walkthroughs and code notebooks."),
            ("Machine Learning", "Advanced", "Deep Learning & Neural Networks Specialization", "https://www.youtube.com/watch?v=aircAruvnKk", "Deep neural networks with TensorFlow and Keras."),
            ("Machine Learning", "Advanced", "MLOps & Model Deployment Pipelines", "https://github.com/GokuMohandas/Made-With-ML", "Deploy models to production, Docker containerization, API creation with FastAPI."),

            ("Data Science", "Beginner", "Intro to Data Science Fundamentals", "https://www.youtube.com/watch?v=ua-CiDNNj30", "Learn Python basics, Pandas, NumPy, and introductory data analysis."),
            ("Data Science", "Beginner", "Python for Data Analysis", "https://www.youtube.com/watch?v=r-uOLxNrNk8", "Hands-on data cleaning, transformation, and visualization tutorial."),
            ("Data Science", "Intermediate", "Exploratory Data Analysis (EDA) Projects", "https://www.youtube.com/watch?v=FNLLxYcUnow", "EDA techniques using Pandas, Seaborn, and Plotly on real datasets."),
            ("Data Science", "Intermediate", "Applied Statistical Modeling", "https://www.youtube.com/watch?v=Vfo5le26bvY", "Hypothesis testing, regression analysis, and confidence intervals."),
            ("Data Science", "Advanced", "Big Data Analytics with Apache Spark", "https://www.youtube.com/watch?v=1vbXmCrkT3Y", "Distributed processing with PySpark DataFrames and MLlib."),
            ("Data Science", "Advanced", "Advanced Feature Engineering Masterclass", "https://github.com/topics/feature-engineering", "Automated feature generation, target encoding, and time series features."),

            ("Web Development", "Beginner", "HTML5, CSS3 & Modern JavaScript Basics", "https://www.youtube.com/watch?v=mU6anWqZJcc", "Learn foundational web development, DOM manipulation, and responsive design."),
            ("Web Development", "Intermediate", "React.js & Full-Stack Web Development", "https://www.youtube.com/watch?v=bMknfKXIFA8", "Component state management, hooks, REST API consumption, and Node.js."),
            ("Web Development", "Advanced", "Full-Stack Microservices & Cloud Deployment", "https://www.youtube.com/watch?v=1xqc65x6P50", "Build microservices with Docker, Kubernetes, CI/CD pipelines, and Next.js."),

            ("Cybersecurity", "Beginner", "Introduction to Cybersecurity & Networking", "https://www.youtube.com/watch?v=inWWhr5tnEA", "Learn network security basics, OSI model, firewalls, and encryption."),
            ("Cybersecurity", "Intermediate", "Ethical Hacking & Web Penetration Testing", "https://www.youtube.com/watch?v=3Kq1MIfTWCE", "OWASP Top 10 vulnerabilities, SQL injection, XSS, and exploit basics."),
            ("Cybersecurity", "Advanced", "Advanced Malware Analysis & Threat Hunting", "https://www.youtube.com/watch?v=7uV8S4dMv10", "Reverse engineering, incident response, SIEM log analysis, and forensics."),

            ("Cloud Computing", "Beginner", "Cloud Computing Fundamentals (AWS/Azure)", "https://www.youtube.com/watch?v=2LaAJq1lB4U", "Core cloud concepts, IaaS vs PaaS vs SaaS, S3 storage, and EC2 instances."),
            ("Cloud Computing", "Intermediate", "DevOps, Docker & Kubernetes Essentials", "https://www.youtube.com/watch?v=3c-iBn73dDE", "Containerization with Docker, Kubernetes orchestration, and CI/CD pipelines."),
            ("Cloud Computing", "Advanced", "Cloud Native Microservices Architecture", "https://www.youtube.com/watch?v=hP15u7P1jB8", "Serverless design, Terraform Infrastructure as Code, and high availability.")
        ]
        for c in courses_seed:
            cursor.execute("INSERT INTO courses (subject, level, title, url, description) VALUES (?, ?, ?, ?, ?)", c)

    conn.commit()
    conn.close()

def get_all_subjects():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT subject FROM courses ORDER BY subject ASC")
    subjects = [row["subject"] for row in cursor.fetchall()]
    conn.close()
    return subjects
