# 🎓 AI-Based Student Learning Path Recommendation System

## Project Overview
A comprehensive **Final Year Project** that uses **Artificial Intelligence and Machine Learning** to analyze student learning patterns and provide **personalized learning path recommendations**. The system predicts a student's learning level (Beginner, Intermediate, or Advanced) based on their academic performance, interest level, and study time commitment.

---

## 🎯 Key Features

### 1. **🔐 User Authentication**
   - Secure login/signup functionality
   - User-specific data persistence
   - Session management

### 2. **📝 Student Assessment Module**
   - Collect student information (name, roll number, subject)
   - Performance metrics input (marks, interest level, study time)
   - AI-powered learning level prediction
   - Confidence score display

### 3. **📊 Personalized Recommendations**
   - **Beginner Level**: Focus on fundamentals and basic concepts
   - **Intermediate Level**: Practical projects and problem-solving
   - **Advanced Level**: Real-world projects and specialization

### 4. **📈 Progress Tracking**
   - Assessment history and records
   - Performance trend analysis
   - Learning pattern visualization
   - Statistics and metrics

### 5. **📚 Learning Resources**
   - Subject-specific resources (books, courses, websites, YouTube channels)
   - Curated content for each learning level
   - Industry-standard materials

### 6. **👤 User Profile Management**
   - Account information
   - Statistics dashboard
   - Quick access links

---

## 🏗️ Project Architecture

### **Technology Stack**
- **Frontend**: Streamlit (Interactive Web UI)
- **Backend**: Python with TensorFlow/Keras
- **ML Algorithm**: Artificial Neural Network (ANN)
- **Clustering**: K-Means Clustering
- **Data Processing**: Scikit-Learn, Pandas, NumPy
- **Visualization**: Matplotlib, Plotly

### **Project Structure**
```
AI_Student_Learning_Path/
├── dataset/
│   ├── app.py              # Main Streamlit application
│   ├── main.py             # Data analysis and exploration
│   ├── train_model.py      # Model training script
│   └── students.csv        # Sample student data
├── model/
│   ├── student_model.h5    # Trained neural network model
│   ├── scaler.pkl          # StandardScaler for data normalization
│   └── level_map.pkl       # Cluster to learning level mapping
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

---

## 📊 Machine Learning Model

### **Data Features**
1. **Marks** (0-100): Student's academic performance
2. **Interest Level** (1-3): Low, Medium, or High engagement
3. **Time Spent** (hours/day): Daily study time commitment

### **Model Architecture**
- **Input Layer**: 3 neurons (features)
- **Hidden Layer 1**: 16 neurons with ReLU activation
- **Hidden Layer 2**: 16 neurons with ReLU activation
- **Output Layer**: 3 neurons with Softmax (3 classes: Beginner, Intermediate, Advanced)

### **Model Performance**
- Algorithm: Artificial Neural Network (Sequential Model)
- Optimizer: Adam
- Loss Function: Sparse Categorical Crossentropy
- Clustering: K-Means (3 clusters)

---

## 🚀 Installation & Setup

### **Prerequisites**
- Python 3.8+
- pip (Python package manager)

### **Step 1: Clone/Download the Project**
```bash
cd AI_Student_Learning_Path
```

### **Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 3: Ensure Model Files Exist**
Check that the following files are present in the `model/` directory:
- `student_model.h5`
- `scaler.pkl`
- `level_map.pkl`

If they don't exist, train the model first:
```bash
python dataset/train_model.py
```

### **Step 4: Run the Application**
```bash
streamlit run dataset/app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 📖 How to Use

### **1. Login/Signup**
- Enter your email and password
- Click "Login" to access the dashboard
- New users can click "Sign Up" (feature coming soon)

### **2. Take an Assessment**
- Go to **Assessment** page
- Fill in your details:
  - Full Name
  - Roll Number
  - Subject/Course
  - Marks obtained (0-100)
  - Interest level (Low/Medium/High)
  - Daily study time (0.5-8 hours)
- Click "Generate Learning Path Recommendation"

### **3. View Recommendations**
- **Personalized Tips**: 6 actionable recommendations based on your level
- **Learning Resources**: Books, courses, websites, and YouTube channels
- **Visualization**: Learning profile and confidence scores

### **4. Track Progress**
- Go to **Progress** page
- View all past assessments
- Analyze trends in marks and study time
- See learning level distribution

### **5. Explore Resources**
- Browse curated resources by subject
- Find recommended books, courses, and learning platforms
- Access quality educational content

### **6. Manage Profile**
- View account information
- Check statistics and achievements
- Update profile settings

---

## 🤖 AI/ML Algorithms Used

### **K-Means Clustering**
- Groups students into 3 clusters based on their performance
- Clusters are mapped to learning levels
- Input: Scaled feature vectors (marks, interest, time spent)

### **Artificial Neural Network (ANN)**
- Deep learning model trained on clustered data
- Predicts learning level from student metrics
- Output: Probability scores for each learning level

### **StandardScaler**
- Normalizes feature values to improve model performance
- Ensures consistent input across predictions

---

## 📊 Sample Dataset

The `dataset/students.csv` contains sample data:

| Student_ID | Subject | Marks | Interest | Time_Spent |
|------------|---------|-------|----------|-----------|
| 1 | Data Science | 78 | High | 2.5 |
| 2 | Data Science | 45 | Medium | 1.2 |
| 3 | Machine Learning | 88 | High | 3.0 |
| ... | ... | ... | ... | ... |

---

## 🎓 Learning Path Recommendations

### **For Beginners 🔴**
- Revise basic concepts thoroughly
- Watch beginner-level tutorials
- Practice simple problems repeatedly
- Take detailed notes on fundamentals
- Ask questions in class/forums
- Build strong foundational knowledge

**Resources**: Khan Academy, YouTube, Textbooks, Practice Sets

### **For Intermediate Level 🟡**
- Work on practical mini-projects
- Solve medium-level problem sets
- Analyze mistakes deeply
- Explore real-world applications
- Collaborate on group projects
- Improve problem-solving strategies

**Resources**: Medium Projects, Case Studies, Online Courses, Peer Learning

### **For Advanced Level 🟢**
- Work on real-world industry projects
- Explore advanced/niche topics
- Contribute to open-source projects
- Aim for mastery and specialization
- Build professional portfolio
- Prepare for advanced certifications

**Resources**: GitHub, Research Papers, Industry Internships, Advanced Courses

---

## 📈 Future Enhancements

- [ ] User authentication with database backend
- [ ] More sophisticated ML models (Random Forest, Gradient Boosting)
- [ ] Real-time progress dashboard
- [ ] Integration with popular learning platforms (Coursera, Udemy)
- [ ] Mobile app version
- [ ] Adaptive learning recommendations
- [ ] Peer comparison analytics
- [ ] Certificate generation upon completion
- [ ] Integration with LMS (Learning Management System)
- [ ] Multi-language support

---

## 🛠️ Technologies & Libraries

| Technology | Version | Purpose |
|-----------|---------|---------|
| Python | 3.8+ | Programming Language |
| Streamlit | 1.28.1 | Web Framework |
| TensorFlow | 2.13.0 | Deep Learning |
| Scikit-Learn | 1.3.0 | Machine Learning |
| Pandas | 2.0.3 | Data Processing |
| NumPy | 1.24.3 | Numerical Computing |
| Matplotlib | 3.7.2 | Visualization |
| Joblib | 1.3.1 | Model Persistence |

---

## 📝 Project Configuration Files

### **requirements.txt**
Contains all Python package dependencies. Install using:
```bash
pip install -r requirements.txt
```

### **.gitignore** (Recommended)
```
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
.env
.venv
env/
venv/
```

---

## 🐛 Troubleshooting

### **Model Not Loading Error**
- Ensure `model/` directory contains all three files: `student_model.h5`, `scaler.pkl`, `level_map.pkl`
- Run `python dataset/train_model.py` to regenerate models

### **Port Already in Use**
```bash
streamlit run dataset/app.py --server.port 8502
```

### **Import Errors**
```bash
pip install --upgrade -r requirements.txt
```

### **Data Not Persisting**
- Data is stored in Streamlit session state (temporary)
- To persist data permanently, integrate a database (SQLite, PostgreSQL)

---

## 👨‍💻 Developer Notes

### **Extending the Project**
1. **Add More Features**: Create new modules in `app.py`
2. **Improve Model**: Retrain with larger dataset in `train_model.py`
3. **Add Database**: Integrate SQLAlchemy for persistence
4. **Deploy**: Use Streamlit Cloud, Heroku, or AWS

### **Code Structure**
- Functions are organized by module (assessment, progress, resources, profile)
- Session state manages user data
- Caching improves performance with `@st.cache_resource`

---

## 📞 Support & Contact

For questions or issues:
1. Check the troubleshooting section above
2. Review the code comments
3. Consult TensorFlow and Streamlit documentation

---

## 📜 License

This is a Final Year Project. Feel free to use and modify as needed for educational purposes.

---

## ✨ Acknowledgments

- **Streamlit**: For the amazing web framework
- **TensorFlow/Keras**: For deep learning capabilities
- **Scikit-Learn**: For ML preprocessing and clustering
- **Python Community**: For excellent libraries and tools

---

**Happy Learning! 🚀**

---

**Last Updated**: March 2026
**Version**: 1.0.0
**Project Type**: Final Year Project (AI/ML)
