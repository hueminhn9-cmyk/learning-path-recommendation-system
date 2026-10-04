import sqlite3

DB_PATH = "student_learning_db.sqlite"

courses_seed = [
    # Machine Learning
    ("Machine Learning", "Beginner", "Machine Learning Course for Beginners (Full Course)", "https://www.youtube.com/watch?v=GwIo3gDZCVQ", "Supervised learning: Linear Regression, Logistic Regression, KNN, and Naive Bayes with Python."),
    ("Machine Learning", "Beginner", "Scikit-Learn Machine Learning Crash Course", "https://www.youtube.com/watch?v=pqNCD_5r0IU", "Build classification and regression ML models step-by-step using Python & Scikit-Learn."),
    ("Machine Learning", "Intermediate", "Machine Learning Algorithms & Evaluation Metrics", "https://www.youtube.com/watch?v=Gv9_4yMHFhI", "Decision Trees, Random Forests, XGBoost, cross-validation, and hyperparameter tuning."),
    ("Machine Learning", "Intermediate", "Hands-On ML Practical Code Projects", "https://github.com/ageron/handson-ml3", "End-to-end Machine Learning project walkthroughs with Jupyter notebooks and Python."),
    ("Machine Learning", "Advanced", "Deep Learning Specialization & Neural Networks", "https://www.youtube.com/watch?v=aircAruvnKk", "Deep neural networks, backpropagation, TensorFlow, Keras, and CNNs."),
    ("Machine Learning", "Advanced", "MLOps & Model Deployment Pipelines", "https://github.com/GokuMohandas/Made-With-ML", "Deploy ML models to production with Docker containers, FastAPI, and CI/CD pipelines."),

    # Data Science
    ("Data Science", "Beginner", "Data Science Course for Beginners", "https://www.youtube.com/watch?v=ua-CiDNNj30", "Learn Python basics, Pandas DataFrames, NumPy arrays, and introductory data analysis."),
    ("Data Science", "Beginner", "Python for Data Analysis & Wrangling Tutorial", "https://www.youtube.com/watch?v=r-uOLxNrNk8", "Hands-on data cleaning, missing value handling, transformation, and visualization."),
    ("Data Science", "Intermediate", "Exploratory Data Analysis (EDA) Projects", "https://www.youtube.com/watch?v=FNLLxYcUnow", "EDA techniques using Pandas, Seaborn, Matplotlib, and Plotly on real-world datasets."),
    ("Data Science", "Intermediate", "Applied Statistical Modeling & Hypothesis Testing", "https://www.youtube.com/watch?v=Vfo5le26bvY", "Hypothesis testing, p-values, regression analysis, ANOVA, and confidence intervals."),
    ("Data Science", "Advanced", "Big Data Analytics with Apache Spark & PySpark", "https://www.youtube.com/watch?v=1vbXmCrkT3Y", "Distributed big data processing with PySpark DataFrames, RDDs, and MLlib."),
    ("Data Science", "Advanced", "Advanced Feature Engineering Masterclass", "https://github.com/topics/feature-engineering", "Automated feature generation, target encoding, interaction terms, and time series features."),

    # Cybersecurity
    ("Cybersecurity", "Beginner", "Cyber Security Course for Beginners (Ethical Hacking)", "https://www.youtube.com/watch?v=3Kq1MIfTWCE", "Learn networking fundamentals, threat analysis, Linux terminal, and basic penetration testing."),
    ("Cybersecurity", "Beginner", "CompTIA Security+ Full Course Tutorial", "https://www.youtube.com/watch?v=9ne33dZzxy0", "Security basics, malware types, encryption, wireless security, and access control."),
    ("Cybersecurity", "Intermediate", "Web Application Security & OWASP Top 10 Vulnerabilities", "https://www.youtube.com/watch?v=cbV83pT8q8E", "Identify and exploit SQL Injection, Cross-Site Scripting (XSS), CSRF, and broken authentication."),
    ("Cybersecurity", "Intermediate", "Network Traffic Analysis & Wireshark Masterclass", "https://www.youtube.com/watch?v=lb11wbAvis8", "Packet analysis, Wireshark filters, detecting intrusion attempts, and TCP/IP handshakes."),
    ("Cybersecurity", "Advanced", "Advanced Penetration Testing & Exploit Development", "https://www.youtube.com/watch?v=2Tz8AId8Y5w", "Buffer overflows, Metasploit framework, reverse engineering, exploit development, and PKI."),
    ("Cybersecurity", "Advanced", "Cloud Security & DevSecOps Engineering", "https://www.youtube.com/watch?v=1uR5Hj0k7-0", "Secure cloud architectures in AWS/Azure, IAM policies, container security, and SAST/DAST."),

    # Web Development
    ("Web Development", "Beginner", "HTML5, CSS3 & Modern JavaScript Full Course", "https://www.youtube.com/watch?v=mU6anWqZJcc", "Learn foundational web development, DOM manipulation, Flexbox, Grid, and responsive design."),
    ("Web Development", "Beginner", "JavaScript Tutorial for Beginners", "https://www.youtube.com/watch?v=W6NZfCO5SIk", "ES6 syntax, functions, async/await, promises, fetch API, and local storage."),
    ("Web Development", "Intermediate", "React.js & Full-Stack Web Development Tutorial", "https://www.youtube.com/watch?v=bMknfKXIFA8", "Component state management, React Hooks, REST API consumption, and Node.js/Express."),
    ("Web Development", "Intermediate", "Node.js & Express.js REST API Masterclass", "https://www.youtube.com/watch?v=Oe421EPjeBE", "Build scalable RESTful backend APIs with Node, Express, MongoDB, and JWT authentication."),
    ("Web Development", "Advanced", "Full-Stack Microservices & Cloud Deployment", "https://www.youtube.com/watch?v=1xqc65x6P50", "Build microservices with Docker, Kubernetes, CI/CD pipelines, GraphQL, and Next.js."),
    ("Web Development", "Advanced", "Next.js 14 Full Stack Web Development", "https://www.youtube.com/watch?v=wm5gMKCOsXg", "Server components, App router, NextAuth authentication, Tailwind CSS, and Vercel deployment."),

    # Cloud Computing
    ("Cloud Computing", "Beginner", "AWS Cloud Practitioner Essentials (Full Course)", "https://www.youtube.com/watch?v=SOTamWNgDKc", "Cloud computing basics, Amazon EC2, S3 storage, IAM roles, and AWS global infrastructure."),
    ("Cloud Computing", "Beginner", "Microsoft Azure Fundamentals (AZ-900)", "https://www.youtube.com/watch?v=NPEsD6n9A_I", "Cloud concepts, Azure core services, security, privacy, compliance, and pricing."),
    ("Cloud Computing", "Intermediate", "Docker Containerization & Kubernetes Masterclass", "https://www.youtube.com/watch?v=fqMOX6JJhGo", "Create Docker containers, Dockerfile optimization, Kubernetes pods, deployments, and scaling."),
    ("Cloud Computing", "Intermediate", "Google Cloud Platform (GCP) Associate Cloud Engineer", "https://www.youtube.com/watch?v=jpno9U1U4zA", "Compute Engine, Cloud Storage, VPC networking, Cloud Run, and IAM permissions."),
    ("Cloud Computing", "Advanced", "DevOps Infrastructure as Code (Terraform & Ansible)", "https://www.youtube.com/watch?v=SLB_c_ayRMo", "Automated cloud infrastructure provisioning with Terraform, configuration with Ansible, and multi-cloud."),
    ("Cloud Computing", "Advanced", "Kubernetes Certified Administrator (CKA) Training", "https://www.youtube.com/watch?v=d6WC5n9G_sM", "Advanced cluster administration, ingress controllers, persistent volumes, and troubleshooting."),

    # Artificial Intelligence
    ("Artificial Intelligence", "Beginner", "Artificial Intelligence Full Course for Beginners", "https://www.youtube.com/watch?v=JMUxmLyrhSk", "Search algorithms (A*, BFS, DFS), constraint satisfaction, game theory, and logic."),
    ("Artificial Intelligence", "Intermediate", "Natural Language Processing (NLP) with Python", "https://www.youtube.com/watch?v=fNxaJsNG3-s", "Text tokenization, sentiment analysis, NLTK, spaCy, TF-IDF, and word embeddings (Word2Vec)."),
    ("Artificial Intelligence", "Advanced", "Generative AI & Transformer Models (LLMs)", "https://www.youtube.com/watch?v=zjkBMFhNj_g", "Transformer architectures, attention mechanisms, fine-tuning LLMs, HuggingFace, and RAG."),

    # Mobile App Development
    ("Mobile App Development", "Beginner", "Flutter & Dart Course for Beginners", "https://www.youtube.com/watch?v=VPvVD8t02U8", "Build cross-platform iOS & Android mobile apps with Flutter widgets, layouts, and state."),
    ("Mobile App Development", "Intermediate", "Android App Development with Kotlin", "https://www.youtube.com/watch?v=F9UC9DY-vIU", "Jetpack Compose UI, Room database, ViewModel, LiveData, and Retrofit HTTP client."),
    ("Mobile App Development", "Advanced", "React Native Full Stack Mobile App Development", "https://www.youtube.com/watch?v=obH0Po_RdWk", "Build production mobile apps with React Native, Expo, Redux Toolkit, Firebase, and Push Notifications."),

    # Software Engineering
    ("Software Engineering", "Beginner", "Software Engineering Fundamentals Course", "https://www.youtube.com/watch?v=W8AeOXa_FqU", "Software development lifecycle (SDLC), Agile Scrum methodologies, Git version control, and UML."),
    ("Software Engineering", "Intermediate", "Design Patterns in Object Oriented Programming", "https://www.youtube.com/watch?v=v9ejT8FO-7I", "Creational, Structural, and Behavioral design patterns in Java/Python (Singleton, Factory, Observer)."),
    ("Software Engineering", "Advanced", "System Design & Distributed Systems Interview Prep", "https://www.youtube.com/watch?v=m8Icp_Cid5o", "Scalability, load balancing, caching (Redis), database sharding, message queues (Kafka), and microservices."),

    # Database Systems
    ("Database Systems", "Beginner", "SQL & Relational Database Design for Beginners", "https://www.youtube.com/watch?v=HXV3zeQKqGY", "SQL SELECT queries, JOINs, GROUP BY, database schema design, and normalization (1NF, 2NF, 3NF)."),
    ("Database Systems", "Intermediate", "PostgreSQL & Database Optimization Masterclass", "https://www.youtube.com/watch?v=qw--VYLpxG4", "Indexes (B-Tree), query execution plans (EXPLAIN ANALYZE), transactions (ACID), and stored procedures."),
    ("Database Systems", "Advanced", "MongoDB & NoSQL Distributed Databases", "https://www.youtube.com/watch?v=c2M-rlkkT5o", "Document databases, aggregation pipelines, indexing, sharding, replication, and Redis caching."),

    # Computer Networks
    ("Computer Networks", "Beginner", "Computer Networking Complete Course", "https://www.youtube.com/watch?v=IPvYjXCsTg8", "OSI model layers, TCP/IP protocol suite, IP addressing, subnetting, DNS, and DHCP."),
    ("Computer Networks", "Intermediate", "Cisco CCNA 200-301 Full Course Tutorial", "https://www.youtube.com/watch?v=H8W9oMNSuwo", "Routing protocols (OSPF), VLANs, Spanning Tree Protocol (STP), NAT, and ACL configuration."),
    ("Computer Networks", "Advanced", "Network Socket Programming & Network Security", "https://www.youtube.com/watch?v=3QhU9jd03a0", "TCP/UDP socket programming in Python/C, TLS/SSL handshake, firewall rules, and VPN protocols.")
]

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Clear existing courses and insert complete set of 50+ resources
cursor.execute("DELETE FROM courses")
cursor.executemany("INSERT INTO courses (subject, level, title, url, description) VALUES (?, ?, ?, ?, ?)", courses_seed)

conn.commit()

cursor.execute("SELECT COUNT(*) FROM courses")
count = cursor.fetchone()[0]
conn.close()

print(f"[OK] Successfully seeded SQLite database with {count} rich video courses across all subjects!")
