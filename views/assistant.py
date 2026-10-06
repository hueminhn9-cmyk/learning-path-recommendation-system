import streamlit as st
import re
from config import IS_VI

def get_detailed_ai_response(query: str, is_vi: bool) -> str:
    """
    Generates a rich, structured, ChatGPT-quality comprehensive answer
    with detailed roadmaps, code snippets, key concepts, recommended resources,
    common pitfalls, and portfolio project suggestions.
    """
    q_lower = query.lower().strip()

    # -------------------------------------------------------------
    # 1. PYTHON & PROGRAMMING ROADMAP
    # -------------------------------------------------------------
    if any(k in q_lower for k in ["python", "pythons", "lộ trình python", "hướng dẫn python"]):
        if is_vi:
            return """🤖 **CHUYÊN GIA AI TƯ VẤN: LỘ TRÌNH HỌC PYTHON TOÀN DIỆN (TỪ 0 ĐẾN DỰ ÁN THỰC TẾ)**

---

### 📌 1. Tổng Quan & Tại Sao Nên Chọn Python?
Python là ngôn ngữ lập trình phổ biến hàng đầu thế giới nhờ **cú pháp ngắn gọn, dễ đọc, thư viện phong phú** và hỗ trợ mạnh mẽ cho các lĩnh vực hot nhất hiện nay: **AI/Machine Learning, Data Science, Web Development, Automation Scripting**.

---

### 🗺️ 2. Lộ Trình Học Chi Tiết 4 Giai Đoạn

| Giai đoạn | Thời gian | Nội dung cốt lõi | Mục tiêu đầu ra |
| :--- | :--- | :--- | :--- |
| **Giai đoạn 1: Nền tảng** | Tuần 1 - 2 | Cú pháp, Biến, Kiểu dữ liệu, Vòng lặp (`for`/`while`), Hàm (`def`), List/Dict/Tuple/Set | Nắm vững tư duy lập trình căn bản |
| **Giai đoạn 2: Lập trình Nâng cao** | Tuần 3 - 4 | OOP (Lớp & Đối tượng), Xử lý File (CSV, JSON), Exception Handling, Virtual Env (`venv`) | Viết code chuẩn mực, sạch sẽ |
| **Giai đoạn 3: Chuyên sâu theo Hướng** | Tháng 2 | **Web:** Flask / FastAPI / Django<br>**Data:** Pandas, NumPy, Matplotlib<br>**AI:** Scikit-Learn, PyTorch | Làm chủ thư viện chuyên ngành |
| **Giai đoạn 4: Đóng gói & Deploy** | Tháng 3 | Git, Docker, RESTful API, Streamlit / Render / Vercel | Đưa sản phẩm lên môi trường Online |

---

### 💻 3. Ví Dụ Code Thực Hành (OOP & Xử Lý Dữ Liệu)

```python
import pandas as pd

class StudentAnalyzer:
    def __init__(self, data_path: str):
        self.df = pd.read_csv(data_path)
    
    def get_top_performers(self, min_gpa: float = 3.5):
        # Lọc ra các sinh viên có GPA cao xuất sắc
        return self.df[self.df['gpa'] >= min_gpa].sort_values(by='gpa', ascending=False)

# Sử dụng class
# analyzer = StudentAnalyzer('students.csv')
# print(analyzer.get_top_performers(3.8))
```

---

### 📚 4. Tài Nguyên & Công Cụ Khuyên Dùng
- 📖 **Sách:** *Automate the Boring Stuff with Python*, *Python Crash Course* (Eric Matthes).
- 🌐 **Nền tảng học:** Coursera (Python for Everybody), RealPython, LeetCode / HackerRank.
- 🛠️ **Công cụ:** VS Code, PyCharm, Jupyter Notebook.

---

### 💡 5. Bẫy Thường Gặp & Mẹo Nâng Cao
- ⚠️ **Lỗi Indentation (Thụt lề):** Python dùng khoảng trắng để định nghĩa block code (dùng 4 spaces, không trộn Tab và Space).
- ⚠️ **Biến Mutability:** Thận trọng khi truyền `list` hoặc `dict` làm tham số mặc định trong hàm (`def foo(items=[])` là anti-pattern!).
- 💡 **Pro Tip:** Hãy luôn dùng `virtualenv` hoặc `conda` để cô lập các gói thư viện cho từng dự án.

---

### 🚀 6. Dự Án Đề Xuất Cho Portfolio
1. 🟡 **Beginner:** Web Scraper cào giá sản phẩm tự động hoặc Tool quản lý chi tiêu cá nhân.
2. 🟢 **Intermediate:** Dashboard phân tích dữ liệu sinh viên tương tác bằng Streamlit.
3. 🔴 **Advanced:** REST API nhận diện khuôn mặt / giọng nói kết hợp FastAPI và OpenCV."""
        else:
            return """🤖 **AI EXPERT ADVISOR: COMPLETE PYTHON ROADMAP (FROM ZERO TO PRODUCTION)**

---

### 📌 1. Overview & Why Learn Python?
Python is the world's most versatile language featuring **clean syntax, readable code, and rich ecosystems** supporting **AI/Machine Learning, Data Science, Web Engineering, and Automation**.

---

### 🗺️ 2. Detailed 4-Phase Roadmap

| Phase | Timeline | Key Curriculum | Outcome Milestone |
| :--- | :--- | :--- | :--- |
| **Phase 1: Fundamentals** | Weeks 1-2 | Syntax, Data Types, Control Flow (`for`/`while`), Functions (`def`), Data Structures | Master core algorithmic thinking |
| **Phase 2: Intermediate** | Weeks 3-4 | OOP (Classes & Objects), File I/O (CSV/JSON), Exception Handling, Virtual Environments | Write clean, modular Python code |
| **Phase 3: Specialization** | Month 2 | **Web:** Flask / FastAPI / Django<br>**Data:** Pandas, NumPy, Matplotlib<br>**AI:** Scikit-Learn, PyTorch | Master domain-specific frameworks |
| **Phase 4: Deployment** | Month 3 | Git, Docker, RESTful APIs, Streamlit / Render / AWS | Deploy production-ready apps |

---

### 💻 3. Practical Code Example (OOP & Data Analysis)

```python
import pandas as pd

class StudentAnalyzer:
    def __init__(self, data_path: str):
        self.df = pd.read_csv(data_path)
    
    def get_top_performers(self, min_gpa: float = 3.5):
        # Filter top performing students by GPA
        return self.df[self.df['gpa'] >= min_gpa].sort_values(by='gpa', ascending=False)
```

---

### 📚 4. Recommended Resources & Tools
- 📖 **Books:** *Automate the Boring Stuff with Python*, *Python Crash Course* (Eric Matthes).
- 🌐 **Platforms:** Coursera (Python for Everybody), RealPython, LeetCode.
- 🛠️ **Tools:** VS Code, PyCharm, Jupyter Notebook.

---

### 💡 5. Pro Tips & Common Pitfalls
- ⚠️ **Mutable Default Arguments:** Avoid `def foo(items=[])`; use `items=None` instead.
- 💡 **Virtual Environments:** Always use `venv` or `conda` to isolate dependencies per project.

---

### 🚀 6. Recommended Portfolio Projects
1. 🟡 **Beginner:** Automated Price Tracker Web Scraper.
2. 🟢 **Intermediate:** Interactive Student Analytics Dashboard with Streamlit.
3. 🔴 **Advanced:** AI Image Recognition REST API with FastAPI and OpenCV."""

    # -------------------------------------------------------------
    # 2. OVERFITTING & MACHINE LEARNING MODEL OPTIMIZATION
    # -------------------------------------------------------------
    elif any(k in q_lower for k in ["overfitting", "underfitting", "quá khớp", "học thuộc lòng", "regularization", "dropout"]):
        if is_vi:
            return """🤖 **CHUYÊN GIA AI TƯ VẤN: KHẮC PHỤC HIỆN TƯỢNG OVERFITTING TRONG MACHINE LEARNING**

---

### 📌 1. Overfitting Là Gì? Vì Sao Lại Xảy Ra?
**Overfitting (Hiện tượng quá khớp / Học thuộc lòng)** xảy ra khi mô hình Machine Learning / Neural Network học quá kỹ toàn bộ dữ liệu huấn luyện — bao gồm cả những nhiễu (noise) và chi tiết ngẫu nhiên không bản chất.

- **Dấu hiệu nhận biết:**
  - `Training Accuracy` rất cao (VD: 99%), `Training Loss` tiệm cận 0.
  - `Validation/Testing Accuracy` lại rất thấp (VD: 60-70%), `Validation Loss` tăng mạnh.

---

### 🗺️ 2. Các Kỹ Thuật Khắc Phục Chi Tiết

| Kỹ thuật | Cơ chế hoạt động | Áp dụng phù hợp cho |
| :--- | :--- | :--- |
| **1. Cross-Validation (K-Fold)** | Chia dữ liệu thành K phần để đánh giá khách quan | Mọi mô hình ML (Random Forest, SVM, XGBoost) |
| **2. Regularization (L1 / L2)** | Thêm thành phần phạt trọng số vào Loss Function: $Loss = Loss_{orig} + \lambda \sum ||w||$ | Linear Models, Logistic Regression, Neural Nets |
| **3. Dropout (0.2 - 0.5)** | Tắt ngẫu nhiên % nút trong mỗi lượt forward pass | Deep Learning & Convolutional Neural Networks |
| **4. Early Stopping** | Theo dõi validation loss và ngắt sớm khi loss không giảm | Neural Networks (TensorFlow, PyTorch) |
| **5. Data Augmentation** | Xoay, lật, méo hình ảnh / biến đổi văn bản để tăng dữ liệu | Computer Vision & Natural Language Processing |

---

### 💻 3. Minh Họa Code Ngăn Overfitting (TensorFlow / Keras)

```python
import tensorflow as tf
from tensorflow.keras import layers, regularizers

model = tf.keras.Sequential([
    # Thêm L2 Regularization
    layers.Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
    
    # Thêm Dropout 30% ngắt kết nối ngẫu nhiên
    layers.Dropout(0.3),
    
    layers.Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
    layers.Dropout(0.2),
    
    layers.Dense(3, activation='softmax')
])

# Callback Dừng sớm (Early Stopping)
early_stop = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss', 
    patience=5, 
    restore_best_weights=True
)

# model.fit(X_train, y_train, validation_data=(X_val, y_val), callbacks=[early_stop])
```

---

### 📚 4. Tài Nguyên Nghiên Cứu Thêm
- 📖 **Tài liệu:** *Deep Learning with Python* (François Chollet), *Hands-On Machine Learning* (Aurélien Géron).
- 🌐 **Khóa học:** DeepLearning.AI Specialization (Andrew Ng - Coursera).

---

### 💡 5. Checklist Kiểm Tra Khi Huấn Luyện Mô Hình
1. ✅ Đã xáo trộn (shuffle) dữ liệu trước khi train/val split chưa?
2. ✅ Đã kiểm tra hiện tượng Data Leakage (lọt thông tin tập test vào tập train) chưa?
3. ✅ Đã thử giảm độ phức tạp của mô hình (giảm số tầng, giảm số cây trong Random Forest) chưa?"""
        else:
            return """🤖 **AI EXPERT ADVISOR: PREVENTING OVERFITTING IN MACHINE LEARNING & DEEP LEARNING**

---

### 📌 1. What is Overfitting & Why Does It Occur?
**Overfitting** happens when a Machine Learning model learns the training dataset (including noise and anomalies) so well that it memorizes rather than generalizes to new data.

- **Key Symptoms:**
  - `Training Accuracy` is extremely high (~99%), `Training Loss` near 0.
  - `Validation/Testing Accuracy` drops significantly (~60-70%), `Validation Loss` spikes upwards.

---

### 🗺️ 2. Comprehensive Remediation Strategies

| Technique | Mechanism | Ideal Use Case |
| :--- | :--- | :--- |
| **1. K-Fold Cross-Validation** | Splits dataset into K folds to validate performance | All ML algorithms (XGBoost, SVM, RF) |
| **2. L1 / L2 Regularization** | Adds penalty term to loss function: $Loss = Loss_{orig} + \lambda \sum ||w||$ | Linear Models, Neural Networks |
| **3. Dropout (20% - 50%)** | Randomly deactivates neurons during forward propagation | Deep Learning & CNNs |
| **4. Early Stopping** | Halts training when validation loss stops improving | Keras, PyTorch training loops |
| **5. Data Augmentation** | Synthesizes new samples via image rotation/flips | Computer Vision & NLP tasks |

---

### 💻 3. Code Example: Implementing Early Stopping & Dropout (Keras)

```python
import tensorflow as tf
from tensorflow.keras import layers, regularizers

model = tf.keras.Sequential([
    layers.Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
    layers.Dropout(0.3),  # Prevents co-adaptation of neurons
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(3, activation='softmax')
])

early_stop = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss', 
    patience=5, 
    restore_best_weights=True
)
```

---

### 📚 4. Recommended Reading
- 📖 *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (Aurélien Géron).
- 🌐 DeepLearning.AI Specialization by Prof. Andrew Ng."""

    # -------------------------------------------------------------
    # 3. WEB FULLSTACK DEVELOPMENT ROADMAP
    # -------------------------------------------------------------
    elif any(k in q_lower for k in ["fullstack", "web", "react", "node", "frontend", "backend", "javascript"]):
        if is_vi:
            return """🤖 **CHUYÊN GIA AI TƯ VẤN: LỘ TRÌNH HỌC LẬP TRÌNH WEB FULLSTACK HIỆN ĐẠI**

---

### 📌 1. Định Nghĩa Web Fullstack
Kỹ sư Web Fullstack là người có khả năng xây dựng toàn bộ hệ thống web: từ giao diện người dùng (**Frontend**), xử lý nghiệp vụ & máy chủ (**Backend**), cho đến lưu trữ dữ liệu (**Database**) và triển khai hệ thống (**DevOps**).

---

### 🗺️ 2. Lộ Trình Chi Tiết Theo Từng Lớp Công Nghệ

```
[ FRONTEND ]   --> HTML5 / CSS3 / ES6+ JavaScript --> React.js / Next.js --> TailwindCSS / Shadcn UI
      │
[ BACKEND ]    --> Node.js (Express) / Python (FastAPI/Django) --> RESTful API & JWT Auth
      │
[ DATABASE ]   --> PostgreSQL / MySQL (Relational) + MongoDB / Redis (NoSQL & Caching)
      │
[ DEVOPS ]     --> Git / GitHub Actions --> Docker Containerization --> Vercel / Render / AWS
```

---

### 💻 3. Ví Dụ RESTful API Với Node.js & Express

```javascript
const express = require('express');
const app = express();
app.use(express.json());

// Endpoint lấy danh sách bài học
app.get('/api/v1/courses', (req, res) => {
    res.status(200).json({
        success: true,
        data: [
            { id: 1, title: 'React Masterclass', level: 'Intermediate' },
            { id: 2, title: 'Node.js Microservices', level: 'Advanced' }
        ]
    });
});

app.listen(5000, () => console.log('🚀 Server running on port 5000'));
```

---

### 📚 4. Bộ Thư Viện & Công Cụ Chuẩn Công Nghiệp
- **Frontend Stack:** React 18, Next.js 14 (App Router), TypeScript, Zustand / Redux Toolkit.
- **Backend Stack:** Node.js, Express.js, Prisma ORM / TypeORM, Passport.js (Authentication).
- **Database:** PostgreSQL, Supabase, MongoDB Atlas, Redis Cloud.

---

### 🚀 5. Gợi Ý Dự Án Portfolio Gây Ấn Tượng Với Nhà Tuyển Dụng
1. 🟡 **Project 1:** Trang e-Commerce đầy đủ giỏ hàng, thanh toán VNPAY/Stripe, Quản lý đơn hàng.
2. 🟢 **Project 2:** Ứng dụng Quản lý công việc Real-time (Trello Clone) với Socket.io.
3. 🔴 **Project 3:** Hệ thống E-learning học trực tuyến tích hợp phát Video & chấm điểm trắc nghiệm."""
        else:
            return """🤖 **AI EXPERT ADVISOR: MODERN FULLSTACK WEB DEVELOPMENT ROADMAP**

---

### 📌 1. Overview
A Fullstack Web Engineer is capable of building end-to-end web applications covering **Frontend UI**, **Backend Business Logic & APIs**, **Databases**, and **Cloud Deployment**.

---

### 🗺️ 2. Step-by-Step Modern Tech Stack

1. **Frontend:** HTML5, CSS3, ES6+ JavaScript, React 18, Next.js 14, TailwindCSS.
2. **Backend:** Node.js (Express) or Python (FastAPI), REST APIs, GraphQL, JWT Authentication.
3. **Database:** PostgreSQL (Relational SQL) & MongoDB (NoSQL) & Redis (Caching).
4. **DevOps & Cloud:** Git, Docker containers, Vercel, Render, AWS S3 / EC2.

---

### 💻 3. Code Example: Express.js REST API

```javascript
const express = require('express');
const app = express();
app.use(express.json());

app.get('/api/v1/courses', (req, res) => {
    res.status(200).json({
        success: true,
        data: [{ id: 1, title: 'React Masterclass', level: 'Intermediate' }]
    });
});

app.listen(5000, () => console.log('Server listening on port 5000'));
```"""

    # -------------------------------------------------------------
    # 4. CYBERSECURITY & NETWORK SECURITY ROADMAP
    # -------------------------------------------------------------
    elif any(k in q_lower for k in ["cybersecurity", "security", "bảo mật", "an toàn thông tin", "hacking", "pentest"]):
        if is_vi:
            return """🤖 **CHUYÊN GIA AI TƯ VẤN: LỘ TRÌNH HỌC AN TOÀN THÔNG TIN & CYBERSECURITY**

---

### 📌 1. Định Hướng Ngành An Toàn Thông Tin
Ngành Bảo mật chia làm 2 nhánh chính:
- 🔵 **Blue Team (Defensive Security):** Giám sát hệ thống, phát hiện xâm nhập (SOC), phản ứng sự cố (Incident Response), củng cố hạ tầng (Hardening).
- 🔴 **Red Team (Offensive Security / Pentest):** Kiểm thử xâm nhập, tìm kiếm lỗ hổng (Vulnerability Assessment), mô phỏng tấn công.

---

### 🗺️ 2. Lộ Trình Chi Tiết 4 Bước Nền Tảng

1. **Bước 1: Nền tảng Mạng (Networking Master):** Mô hình OSI 7 lớp, TCP/IP, Router/Switch, DNS, DHCP, HTTP/HTTPS, VPN, Wireshark.
2. **Bước 2: Hệ Điều Hành & Command Line:** Sử dụng Kali Linux, Ubuntu Server, PowerShell, Bash Scripting.
3. **Bước 3: Lỗ Hổng Web (OWASP Top 10):** SQL Injection, XSS, CSRF, Broken Auth, SSRF, IDOR.
4. **Bước 4: Công Cụ & Chứng Chỉ Chuyên Nghiệp:** Nmap, Burp Suite, Metasploit, Wireshark, chứng chỉ CompTIA Security+, CEH, OSCP.

---

### 💻 3. Minh Họa Code Python Kiểm Tra Lỗi SQL Injection (Educational Purpose)

```python
import requests

def test_sqli(url: str):
    # Kiểm tra phản ứng của URL với payload SQLi đơn giản
    payload = "' OR '1'='1"
    target = f"{url}?id={payload}"
    response = requests.get(target)
    
    if "syntax error" in response.text.lower() or "mysql" in response.text.lower():
        print("⚠️ Có khả năng dính lỗ hổng SQL Injection!")
    else:
        print("✅ Kiểm tra an toàn sơ bộ.")
```

---

### 📚 4. Nền Tảng Thực Hành Luyện Tập An Toàn
- 🎯 TryHackMe (Cực kỳ phù hợp cho người mới bắt đầu)
- 🎯 Hack The Box (Phù hợp level Intermediate & Advanced)
- 🎯 PortSwigger Web Security Academy (Trùm về Web Security miễn phí)"""
        else:
            return """🤖 **AI EXPERT ADVISOR: CYBERSECURITY & ETHICAL HACKING ROADMAP**

---

### 📌 1. Overview
Cybersecurity is categorized into:
- 🔵 **Blue Team (Defense):** SOC Analysis, Incident Response, Network Hardening.
- 🔴 **Red Team (Offensive):** Penetration Testing, Vulnerability Research, Red Teaming.

---

### 🗺️ 2. Core Roadmap
1. **Networking Fundamentals:** OSI Model, TCP/IP, DNS, Subnetting, Wireshark.
2. **OS Mastery:** Linux CLI (Kali/Ubuntu), Bash Scripting, Windows Internals.
3. **Web Security:** OWASP Top 10 (SQLi, XSS, CSRF, SSRF, IDOR).
4. **Tools & Certifications:** Burp Suite, Nmap, Metasploit, CompTIA Security+, OSCP.

---

### 📚 3. Practice Labs
- TryHackMe, Hack The Box, PortSwigger Web Security Academy."""

    # -------------------------------------------------------------
    # 5. DATA SCIENCE & MACHINE LEARNING / AI ROADMAP
    # -------------------------------------------------------------
    elif any(k in q_lower for k in ["data science", "machine learning", "trí tuệ nhân tạo", "ai", "deep learning", "khoa học dữ liệu"]):
        if is_vi:
            return """🤖 **CHUYÊN GIA AI TƯ VẤN: LỘ TRÌNH KHOA HỌC DỮ LIỆU & TRÍ TUỆ NHÂN TẠO (AI/ML)**

---

### 📌 1. Tổng Quan Về AI / Machine Learning / Data Science
Lĩnh vực AI đòi hỏi sự kết hợp giữa **Toán học (Đại số tuyến tính, Giải tích, Xác suất thống kê)**, **Kỹ năng Lập trình (Python/R)** và **Tư duy Nghiệp vụ (Business Understanding)**.

---

### 🗺️ 2. Lộ Trình Học Chi Tiết 5 Cột Mốc

```
[ TOÁN NỀN TẢNG ]   --> Đại số tuyến tính, Xác suất thống kê, Giải tích ma trận
       │
[ PYTHON FOR DATA ] --> NumPy, Pandas (Biến đổi dữ liệu), Matplotlib/Seaborn (Trực quan hóa)
       │
[ MACHINE LEARNING ]--> Regression, Classification, Clustering, Random Forest, XGBoost (Scikit-Learn)
       │
[ DEEP LEARNING ]   --> ANN, CNN (Xử lý ảnh), RNN/LSTM (Chuỗi thời gian), Transformer (PyTorch/TensorFlow)
       │
[ GENERATIVE AI ]   --> LLM Fine-tuning, RAG (Retrieval-Augmented Generation), LangChain, Vector DB (Chroma/Pinecone)
```

---

### 💻 3. Code Minh Họa Huấn Luyện Mô Hình Random Forest

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

# Load dữ liệu
df = pd.read_csv('dataset/students.csv')
X = df[['marks', 'interest_num', 'study_hours']]
y = df['target_level']

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Đánh giá
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
```

---

### 📚 4. Tài Nguyên Hàng Đầu Khuyên Dùng
- 🎓 **Khóa học:** Machine Learning Specialization (Andrew Ng - Stanford / Coursera).
- 🏆 **Sân chơi:** Kaggle Competitions & Datasets.
- 📖 **Sách:** *Pattern Recognition and Machine Learning* (Christopher Bishop)."""
        else:
            return """🤖 **AI EXPERT ADVISOR: DATA SCIENCE & ARTIFICIAL INTELLIGENCE ROADMAP**

---

### 📌 1. Overview
Data Science & AI require a blend of **Mathematics (Linear Algebra, Calculus, Statistics)**, **Software Engineering (Python)**, and **Domain Knowledge**.

---

### 🗺️ 2. 5-Stage Learning Roadmap
1. **Math Foundations:** Linear Algebra, Calculus, Probability & Statistics.
2. **Python Data Ecosystem:** Pandas, NumPy, Matplotlib, Seaborn.
3. **Machine Learning:** Scikit-Learn (Regression, Decision Trees, XGBoost).
4. **Deep Learning:** Neural Networks, CNNs, Transformers using PyTorch or TensorFlow.
5. **Generative AI & LLMs:** LangChain, RAG Architecture, Vector DBs (ChromaDB/Pinecone).

---

### 💻 3. Code Example: Scikit-Learn Random Forest

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)
```"""

    # -------------------------------------------------------------
    # 6. ALGORITHMS, DATA STRUCTURES & LEETCODE
    # -------------------------------------------------------------
    elif any(k in q_lower for k in ["thuật toán", "cấu trúc dữ liệu", "leetcode", "algorithm", "data structure", "dsa"]):
        if is_vi:
            return """🤖 **CHUYÊN GIA AI TƯ VẤN: BÍ QUYẾT CHINH PHỤC CẤU TRÚC DỮ LIỆU & THUẬT TOÁN (DSA)**

---

### 📌 1. Tầm Quan Trọng Của DSA
Cấu trúc dữ liệu & Thuật toán là gốc rễ của mọi hệ thống phần mềm hiệu năng cao và là nội dung phỏng vấn cốt lõi của các tập đoàn công nghệ (Big Tech / FAANG).

---

### 🗺️ 2. Danh Sách Các Chủ Đề Bắt Buộc Phải Nắm

| Nhóm chủ đề | Cấu trúc dữ liệu / Thuật toán cốt lõi | Độ phức tạp thời gian phổ biến |
| :--- | :--- | :--- |
| **Array & String** | Two Pointers, Sliding Window, Prefix Sum | $O(N)$ |
| **Linked List & Stack/Queue** | Reverse LinkedList, Fast & Slow Pointers, Monotonic Stack | $O(N)$ |
| **Tree & Graph** | Binary Search Tree (BST), DFS, BFS, Dijkstra, Topological Sort | $O(V + E)$ |
| **Sorting & Searching** | Binary Search, QuickSort, MergeSort | $O(N \\log N)$ |
| **Dynamic Programming (DP)** | Memoization, Tabulation, 0/1 Knapsack, Coin Change | $O(N \\cdot M)$ |

---

### 💻 3. Minh Họa Thuật Toán Binary Search Trong Python

```python
def binary_search(arr: list[int], target: int) -> int:
    # Tìm kiếm nhị phân với độ phức tạp O(log N)
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1 # Không tìm thấy
```

---

### 💡 4. Chiến Lược Luyện LeetCode Hiệu Quả
- 🎯 Không giải dàn trải. Hãy tập trung luyện danh sách **Blind 75** hoặc **NeetCode 150**.
- ⏱️ Mỗi bài giới hạn giải trong **30-45 phút**. Nếu tắc ý tưởng, hãy đọc phần Solution để hiểu Pattern rồi tự code lại.
- 📝 Viết lại phân tích Time Complexity $O(N)$ và Space Complexity $O(1)$ cho mọi bài đã giải."""
        else:
            return """🤖 **AI EXPERT ADVISOR: DATA STRUCTURES & ALGORITHMS (DSA) MASTERCLASS**

---

### 📌 1. Overview
DSA forms the foundation of high-performance software engineering and technical interviews at top tech companies.

---

### 🗺️ 2. Essential Curriculum & Patterns
- **Array & Strings:** Two Pointers, Sliding Window ($O(N)$).
- **Trees & Graphs:** DFS, BFS, Dijkstra's Algorithm ($O(V+E)$).
- **Dynamic Programming:** Memoization, Tabulation ($O(N \\cdot M)$).

---

### 💡 3. LeetCode Practice Strategy
- Focus on the **NeetCode 150** or **Blind 75** curated lists.
- Time box problem solving to 30-45 minutes before analyzing solutions."""

    # -------------------------------------------------------------
    # 7. STUDY TIPS, EXAM PREPARATION & GENERAL QUESTIONS
    # -------------------------------------------------------------
    else:
        if is_vi:
            return f"""🤖 **CHUYÊN GIA AI TƯ VẤN: PHÂN TÍCH & GIẢI ĐÁP CHI TIẾT CHO CÂU HỎI**

> ❓ **Câu hỏi của bạn:** *"{query}"*

---

### 📌 1. Tổng Quan & Phân Tích Cốt Lõi
Chủ đề bạn vừa hỏi đóng vai trò rất quan trọng trong quá trình phát triển tư duy học tập và kỹ năng thực hành. Để hiểu sâu và ứng dụng hiệu quả, bạn cần nắm rõ nguyên lý hoạt động và các trường hợp sử dụng cụ thể.

---

### 🗺️ 2. Phương Pháp & Lộ Trình 4 Bước Đề Xuất

```
[ BƯỚC 1: NẮM KHÁI NIỆM GỐC ]   --> Đọc tài liệu chuẩn & Hiểu rõ bản chất vấn đề
       │
[ BƯỚC 2: THỰC HÀNH MÔ HÌNH NHỎ ] --> Tạo các bài tập thử nghiệm / Mini-demo
       │
[ BƯỚC 3: PHÂN TÍCH & ĐÁNH GIÁ ]  --> Kiểm tra kết quả, phát hiện lỗi & tối ưu
       │
[ BƯỚC 4: ỨNG DỤNG VÀO DỰ ÁN ]    --> Đóng gói thành sản phẩm thực tế trong Portfolio
```

---

### 💡 3. Các Lời Khuyên Hàng Đầu Từ AI Advisor

1. 🎯 **Kỹ Thuật Học Pomodoro (25/5):** Tập trung tuyệt đối 25 phút, nghỉ 5 phút để giữ não bộ ở trạng thái tối ưu.
2. 📝 **Phương Pháp Feynman:** Hãy thử giải thích lại khái niệm này cho một người chưa biết gì bằng ngôn ngữ đơn giản nhất. Nếu bạn giải thích được, bạn đã thực sự hiểu nó!
3. 🛠️ **Thực Hành Hàng Ngày (Active Recall & Spaced Repetition):** Đừng chỉ đọc suông tài liệu. Hãy tự đặt câu hỏi và gõ code thực tế.

---

### 📚 4. Gợi Ý Các Chủ Đề Tiếp Theo Bạn Có Thể Hỏi AI
- *"Cho tôi danh sách các khóa học miễn phí chất lượng về chủ đề này?"*
- *"Hãy cho tôi bài tập thực hành mẫu có đáp án chi tiết?"*
- *"Làm sao để đưa kiến thức này vào hồ sơ xin việc (CV)?"*"""
        else:
            return f"""🤖 **AI EXPERT ADVISOR: COMPREHENSIVE ANSWER & INSIGHTS**

> ❓ **Your Prompt:** *"{query}"*

---

### 📌 1. Overview & Core Concept
Understanding this topic requires breaking it down into structural components, practical applications, and best practices.

---

### 🗺️ 2. 4-Step Master Plan

1. **Step 1: Core Theory & Principles** - Master fundamental terminology and mechanics.
2. **Step 2: Hands-On Experimentation** - Build small isolated practice modules.
3. **Step 3: Review & Optimization** - Analyze performance, fix bugs, refine execution.
4. **Step 4: Real-World Portfolio Integration** - Combine skills into a production project.

---

### 💡 3. Pro Tips for Rapid Learning
- 🎯 **Feynman Technique:** Explain the concept in simple terms without jargon.
- 📝 **Active Recall:** Build practice tests rather than passively re-reading notes.
- ⏱️ **Pomodoro Method:** Use 25-minute focused blocks for deep work sessions."""


def ai_assistant_page():
    st.markdown(f"""
    <div class="hero-banner">
        <span class="hero-badge">🤖 Smart ChatGPT-Level AI Assistant</span>
        <h1 style="margin:8px 0; font-size:2.2rem; font-weight:800;">
            {"Trợ lý AI Hỏi đáp & Tư vấn Học tập Chuyên sâu" if IS_VI() else "Smart AI Study & Technical Advisor"}
        </h1>
        <p style="font-size:1.05rem; opacity:0.95; margin:0;">
            {"Hỏi đáp mọi thắc mắc về Lộ trình học, Khái niệm AI/ML, Code, Bảo mật, Cấu trúc dữ liệu & Định hướng sự nghiệp" if IS_VI() else "Ask anything about Roadmaps, AI/ML concepts, Code debugging, Cybersecurity, Algorithms & Career guidance"}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Initialize Chat History
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {
                "role": "assistant", 
                "content": (
                    "👋 **Xin chào! Tôi là Trợ lý AI Hỏi đáp Học tập Chuyên sâu (ChatGPT-Style Advisor).**\n\n"
                    "Bạn có thể chọn các câu hỏi gợi ý bên dưới hoặc tự nhập câu hỏi bất kỳ về:\n"
                    "- 🐍 **Lộ trình học Lập trình (Python, Web Fullstack, C++, Java)**\n"
                    "- 🧠 **AI, Machine Learning, Deep Learning & Overfitting**\n"
                    "- 🛡️ **Cybersecurity, Linux & DevOps**\n"
                    "- 📊 **Cấu trúc Dữ liệu, Thuật toán & LeetCode**\n"
                    "- 💡 **Phương pháp học tập & Bí quyết luyện thi hiệu quả**"
                    if IS_VI() else
                    "👋 **Hello! I am your AI Study Advisor (ChatGPT-Style Technical Assistant).**\n\n"
                    "Feel free to click prompt buttons below or type any question regarding programming roadmaps, AI/ML models, algorithm optimization, cybersecurity, or study strategies!"
                )
            }
        ]

    # Upper Bar: Quick Category Tabs & Utility Buttons
    top_col1, top_col2 = st.columns([3, 1])
    with top_col1:
        st.markdown(f"##### 💡 **{'Gợi ý câu hỏi phổ biến theo chủ đề:' if IS_VI() else 'Quick Prompts by Topic:'}**")
    with top_col2:
        if st.button("🗑️ " + ("Xóa lịch sử Chat" if IS_VI() else "Clear History"), use_container_width=True, key="del_chat"):
            st.session_state.chat_history = []
            st.rerun()

    # Categorized Prompt Buttons
    prompt_selected = None

    prompt_tabs = st.tabs([
        "🐍 Python & Data" if IS_VI() else "🐍 Python & Data",
        "🧠 AI & ML" if IS_VI() else "🧠 AI & ML",
        "🌐 Web Fullstack" if IS_VI() else "🌐 Web Fullstack",
        "🛡️ Cybersecurity" if IS_VI() else "🛡️ Security",
        "📊 Thuật toán DSA" if IS_VI() else "📊 DSA & Algorithms"
    ])

    with prompt_tabs[0]:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🚀 " + ("Lộ trình học Python từ 0 đến Dự án" if IS_VI() else "Python Roadmap from Zero"), use_container_width=True):
                prompt_selected = "Cho tôi lộ trình học Python từ cơ bản đến nâng cao và tạo dự án thực tế?" if IS_VI() else "Give me a step-by-step Python roadmap from beginner to advanced with projects?"
        with col2:
            if st.button("📊 " + ("Lộ trình trở thành Data Scientist" if IS_VI() else "Data Science Roadmap"), use_container_width=True):
                prompt_selected = "Lộ trình học Data Science và Machine Learning từng bước như thế nào?" if IS_VI() else "What is the step-by-step roadmap to become a Data Scientist?"

    with prompt_tabs[1]:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⚡ " + ("Cách khắc phục Overfitting trong AI" if IS_VI() else "Fix Overfitting in ML"), use_container_width=True):
                prompt_selected = "Overfitting trong AI là gì và cách khắc phục chi tiết?" if IS_VI() else "What is Overfitting in ML and how to fix it with code examples?"
        with col2:
            if st.button("🤖 " + ("So sánh PyTorch vs TensorFlow" if IS_VI() else "PyTorch vs TensorFlow"), use_container_width=True):
                prompt_selected = "Học Deep Learning nên chọn PyTorch hay TensorFlow?" if IS_VI() else "Should I learn PyTorch or TensorFlow for Deep Learning?"

    with prompt_tabs[2]:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🌐 " + ("Lộ trình Web Fullstack Modern" if IS_VI() else "Fullstack Web Roadmap"), use_container_width=True):
                prompt_selected = "Lập trình Web Fullstack cần học những công nghệ gì?" if IS_VI() else "What tech stack to learn for Fullstack Web Development?"
        with col2:
            if st.button("⚙️ " + ("Xây dựng RESTful API chuẩn" if IS_VI() else "RESTful API Best Practices"), use_container_width=True):
                prompt_selected = "Các nguyên tắc xây dựng RESTful API chuẩn công nghiệp?" if IS_VI() else "What are the core principles of building RESTful APIs?"

    with prompt_tabs[3]:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🛡️ " + ("Bắt đầu học Cybersecurity" if IS_VI() else "Start Cybersecurity"), use_container_width=True):
                prompt_selected = "Bắt đầu học Cybersecurity cần những kiến thức và công cụ gì?" if IS_VI() else "What skills and tools are needed to start learning Cybersecurity?"
        with col2:
            if st.button("🔥 " + ("Top 10 Lỗ hổng Web OWASP" if IS_VI() else "OWASP Top 10 Web Vulnerabilities"), use_container_width=True):
                prompt_selected = "Giải thích các lỗ hổng OWASP Top 10 phổ biến nhất?" if IS_VI() else "Explain the OWASP Top 10 web vulnerabilities?"

    with prompt_tabs[4]:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💡 " + ("Bí quyết luyện LeetCode hiệu quả" if IS_VI() else "LeetCode Practice Strategy"), use_container_width=True):
                prompt_selected = "Phương pháp học Cấu trúc Dữ liệu & Thuật toán và luyện LeetCode hiệu quả?" if IS_VI() else "How to study Data Structures & Algorithms and practice LeetCode effectively?"
        with col2:
            if st.button("⏱️ " + ("Giải thích độ phức tạp Time Complexity O(N)" if IS_VI() else "Time Complexity O(N) Explanation"), use_container_width=True):
                prompt_selected = "Độ phức tạp thời gian Big-O là gì và cách tính O(N), O(log N)?" if IS_VI() else "What is Big-O notation and how to calculate Time Complexity?"

    st.markdown("---")

    # Display Chat Messages Container
    chat_container = st.container()

    with chat_container:
        for msg in st.session_state.chat_history:
            avatar = "🤖" if msg["role"] == "assistant" else "👤"
            with st.chat_message(msg["role"], avatar=avatar):
                st.markdown(msg["content"])

    # User Chat Input
    user_input = st.chat_input("Nhập câu hỏi chi tiết cho Trợ lý AI (ChatGPT-Style)..." if IS_VI() else "Type your detailed question for AI Assistant...")

    # Determine Active Input (From Clicked Prompt or Chat Input)
    active_query = prompt_selected or user_input

    if active_query:
        # Append User Message
        st.session_state.chat_history.append({"role": "user", "content": active_query})
        with st.chat_message("user", avatar="👤"):
            st.markdown(active_query)

        # Generate Detailed AI Response
        with st.spinner("🤖 AI Assistant đang suy nghĩ và tổng hợp câu trả lời chi tiết..." if IS_VI() else "🤖 AI Assistant is processing a detailed response..."):
            ai_reply = get_detailed_ai_response(active_query, IS_VI())

        # Append & Render Assistant Message
        st.session_state.chat_history.append({"role": "assistant", "content": ai_reply})
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(ai_reply)

        # Force rerun to keep scroll at bottom
        st.rerun()
