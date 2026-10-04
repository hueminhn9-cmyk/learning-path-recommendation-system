# 🎓 AI Student Learning Path Recommendation System - User Guide

## ✅ System is Now Live!

Your application is running successfully at:
- **Local URL**: http://localhost:8502
- **Network URL**: http://192.168.1.75:8502

---

## 📱 Frontend Application Features

### **Module 1: Authentication System** 🔐
**Location**: Login Page (First Screen)

**Features:**
- Email-based user authentication
- Password-protected access
- Session management
- User profile creation

**How to Use:**
1. Enter your email address
2. Enter your password
3. Click "🔐 Login" button
4. Sign up feature coming soon

**Default Test Credentials:**
- Email: `student@college.edu`
- Password: `any password` (demo accepts any input)

---

### **Module 2: Dashboard/Home Page** 🏠
**Location**: Navigation → Home

**Features:**
- Personalized welcome message
- Quick feature overview
- Real-time statistics
- Assessment summary

**What You See:**
- ✨ Key Features (AI Analysis, Personalized Path, Progress Tracking)
- 📈 Quick Stats (Total Assessments, Average Marks, Study Time, Latest Level)
- 👋 Personalized greeting with your name
- 📊 Current date and time

---

### **Module 3: Student Assessment** 📝
**Location**: Navigation → Assessment

**Key Features:**

#### **Part A: Student Information**
- Full Name input
- Roll Number input
- Subject/Course selection
  - Data Science
  - Machine Learning
  - Big Data
  - Deep Learning
  - Web Development
  - Cloud Computing

#### **Part B: Performance Metrics**
- **Marks Obtained** (0-100)
  - Slider input for ease of use
  - Step: 5 marks

- **Interest Level**
  - Low: Less engaged in subject
  - Medium: Moderate engagement
  - High: Very engaged in subject

- **Study Time** (0.5-8 hours/day)
  - Daily time commitment to learning
  - Step: 0.5 hours

#### **Assessment Summary**
Before generating recommendations, you'll see:
- 📊 Your marks
- 🔥 Your interest level
- ⏱ Your daily study time

#### **AI Prediction**
Clicking "🤖 Generate Learning Path Recommendation" will:
1. Send data to the AI model
2. Predict your learning level
3. Calculate confidence score
4. Generate personalized recommendations

---

### **Module 4: Personalized Recommendations** 🎯
**Displayed After Assessment**

**For Beginners 🔴 (Low Performance)**
```
Learning Level: Beginner
Recommended Actions:
✅ Revise all basic concepts thoroughly
✅ Watch beginner-level tutorials
✅ Practice simple problems repeatedly
✅ Take detailed notes on fundamentals
✅ Ask questions in class/forums
✅ Build strong foundational knowledge

Resources:
• Khan Academy
• YouTube Tutorials
• Textbooks
• Practice Sets
```

**For Intermediate 🟡 (Medium Performance)**
```
Learning Level: Intermediate
Recommended Actions:
✅ Work on practical mini-projects
✅ Solve medium-level problem sets
✅ Analyze your mistakes deeply
✅ Explore real-world applications
✅ Collaborate on group projects
✅ Improve problem-solving strategies

Resources:
• Medium Projects
• Case Studies
• Online Courses
• Peer Learning
```

**For Advanced 🟢 (High Performance)**
```
Learning Level: Advanced
Recommended Actions:
✅ Work on real-world industry projects
✅ Explore advanced/niche topics
✅ Contribute to open-source projects
✅ Aim for mastery and specialization
✅ Build a professional portfolio
✅ Prepare for advanced certifications

Resources:
• GitHub
• Research Papers
• Industry Internships
• Advanced Courses
```

---

### **Module 5: Progress Tracking** 📈
**Location**: Navigation → Progress

**Features:**

#### **Assessment History Table**
View all your past assessments with:
- Student Name
- Roll Number
- Subject
- Marks obtained
- Interest level
- Study time
- Predicted learning level
- Model confidence
- Date and time

#### **Performance Trends**
View visual charts showing:
1. **Marks Progression**: Line chart of marks over assessments
2. **Study Time Progression**: Line chart of study hours over time
3. **Learning Level Distribution**: Bar chart showing count of each level
4. **Interest Level Distribution**: Pie chart showing interest percentages

**Use Cases:**
- Track your academic progress
- Identify improvement trends
- Analyze study habits
- Monitor learning level changes

---

### **Module 6: Learning Resources** 📚
**Location**: Navigation → Resources

**Features:**
- Subject-specific learning materials
- Curated by education experts
- Multiple resource types

**Subjects Available:**
1. **Data Science**
   - Books: Python for Data Analysis, Data Science from Scratch, etc.
   - Online Courses: Coursera, Udacity, DataCamp
   - Websites: Kaggle, Analytics Vidhya, Medium
   - YouTube: StatQuest, Krish Naik, Code Basics

2. **Machine Learning**
   - Books: Hands-On ML, Pattern Recognition, Deep Learning
   - Courses: Andrew Ng Course, Fast.ai, Coursera
   - Websites: ML Mastery, Medium, Distill
   - YouTube: 3Blue1Brown, StatQuest, Sentdex

3. **Big Data**
   - Books: Hadoop Guide, Spark Guide, Learning Spark
   - Courses: Coursera, Udemy, CloudxLab
   - Websites: Databricks, Apache.org, Medium
   - YouTube: CloudxLab, Learn Big Data, Data Science Central

4. **Deep Learning**
   - Books: Deep Learning Book, Neural Networks, TensorFlow Guide
   - Courses: Deep Learning AI, Fast.ai, TensorFlow
   - Websites: TensorFlow.org, PyTorch.org, Papers With Code
   - YouTube: 3Blue1Brown, Sentdex, Jeremy Howard

**How to Use:**
1. Select a subject from dropdown
2. Browse recommended resources by category
3. Books, Courses, Websites, and YouTube Channels
4. Click links to access external resources

---

### **Module 7: User Profile** 👤
**Location**: Navigation → Profile

**Features:**

#### **Account Information**
- Email address
- Username
- Member since date

#### **Profile Statistics**
- Total number of assessments taken
- Average marks across all assessments
- Current learning level

#### **Quick Links**
- 📝 Take Assessment
- 📈 View Progress
- 📚 Learning Resources
- ⚙️ Settings (coming soon)

---

## 🎯 How to Get Started

### **Step 1: Login**
```
1. Open http://localhost:8502 in your browser
2. Enter any email: student@college.edu
3. Enter any password
4. Click "Login"
```

### **Step 2: Take Your First Assessment**
```
1. Click "📝 Assessment" in sidebar
2. Fill in your details:
   - Name: Your full name
   - Roll: Your roll number
   - Subject: Choose your subject
   - Marks: Enter marks (0-100)
   - Interest: Select level (Low/Medium/High)
   - Study Time: Set daily study hours
3. Click "🤖 Generate Learning Path Recommendation"
```

### **Step 3: View Recommendations**
```
1. See your predicted learning level
2. Check confidence score
3. Read personalized tips
4. Review suggested resources
5. View learning profile visualization
```

### **Step 4: Track Progress**
```
1. Take multiple assessments
2. Click "📈 Progress" to see trends
3. Analyze your performance
4. Monitor learning improvements
```

### **Step 5: Explore Resources**
```
1. Click "📚 Resources"
2. Select your subject
3. Browse books, courses, websites
4. Find learning materials
```

---

## 🔧 Sidebar Navigation

The left sidebar always shows:

```
🗺️ Navigation
━━━━━━━━━━━━━
🏠 Home
📝 Assessment
📈 Progress
📚 Resources
👤 Profile

━━━━━━━━━━━━━
👤 Logged in as: [Your Name]
📧 Email: [Your Email]

[🚪 Logout Button]
```

**Quick Access Tips:**
- Click any option to navigate instantly
- Your session data persists within the current login
- Logout to clear session and login again

---

## 📊 AI Model Information

### **How the Prediction Works:**

1. **Input Data Collection**
   - Your marks (0-100)
   - Interest level (1-3)
   - Study time (hours/day)

2. **Data Preprocessing**
   - Normalization using StandardScaler
   - Feature scaling for consistency

3. **AI Analysis**
   - Neural Network processes data
   - 3 hidden layers with ReLU activation
   - 3 output predictions (Beginner, Intermediate, Advanced)

4. **Prediction**
   - Model calculates probability for each level
   - Highest probability is your predicted level
   - Confidence shown as percentage

5. **Recommendations**
   - Custom tips based on your level
   - Curated resources matched to your needs
   - Visualization of your learning profile

---

## 💾 Data Management

### **Session State**
- Your assessments are stored in session memory
- Persists while you're logged in
- Clears when you logout

### **Persistent Storage** (Future Feature)
- Integration with database planned
- Will save all your records permanently
- Access history from any device

---

## 🎨 UI/UX Features

### **Color Scheme**
- 🔴 **Red**: Beginner level (needs more foundation)
- 🟡 **Yellow**: Intermediate level (good progress)
- 🟢 **Green**: Advanced level (excellent performance)
- 🔵 **Blue**: Primary actions and headers

### **Icons Used**
- 🎓 Education/Learning
- 📊 Statistics/Data
- 📈 Progress/Trends
- 📚 Resources/Books
- 👤 Profile/User
- 🔐 Security/Login
- 🤖 AI/Intelligence
- ✅ Checkmarks/Success

### **Responsive Design**
- Works on desktop and tablet
- Mobile optimization coming soon
- Two-column layout for detailed views
- Single-column layout for simple views

---

## ⚙️ Settings & Customization

### **Current Settings**
- Page layout: Wide (optimized for desktop)
- Theme: Default Streamlit theme
- Font size: Auto-responsive

### **Future Customization Options**
- Dark mode / Light mode toggle
- Font size adjustment
- Subject preferences
- Notification settings

---

## 🐛 Troubleshooting

### **Problem: Page not loading**
**Solution:**
1. Refresh browser (Ctrl+R)
2. Clear browser cache
3. Close and reopen Streamlit

### **Problem: Assessment not saving**
**Solution:**
1. Ensure all fields are filled
2. Check internet connection
3. Model files should exist in `model/` folder

### **Problem: Graphs not displaying**
**Solution:**
1. Refresh the page
2. Click back and return to page
3. Check browser's JavaScript is enabled

### **Problem: Slow predictions**
**Solution:**
1. This is normal for first prediction (model loading)
2. Subsequent predictions are faster
3. Check system resources

### **Problem: "Model not loaded" error**
**Solution:**
1. Run: `python dataset/train_model.py`
2. Ensure files exist in `model/` folder:
   - student_model.h5
   - scaler.pkl
   - level_map.pkl

---

## 📈 Key Metrics & Visualizations

### **Learning Profile Chart**
Shows:
- Your marks (out of 100)
- Your interest level (0-3)
- Your study time (in hours)

### **Confidence Gauge**
Shows:
- Model's confidence in prediction
- 0-100% scale
- Reference point at 80%

### **Trend Analysis**
Shows:
- Marks progression over time
- Study time changes
- Level distribution
- Interest level statistics

---

## 🎓 Learning Level Descriptions

### **Beginner 🔴**
- Marks: Generally 0-40
- Focus: Building foundations
- Recommendation: Core concepts, basic practice
- Timeline: 3-6 months to intermediate

### **Intermediate 🟡**
- Marks: Generally 40-75
- Focus: Practical application
- Recommendation: Projects, problem-solving
- Timeline: 2-4 months to advanced

### **Advanced 🟢**
- Marks: Generally 75-100
- Focus: Mastery and specialization
- Recommendation: Industry projects, research
- Timeline: Continuous improvement

---

## 💡 Tips for Best Results

1. **Be Honest with Input**
   - Enter accurate marks
   - Realistic interest level
   - True study time

2. **Regular Assessments**
   - Take assessments periodically
   - Track your progress
   - Adjust study strategy

3. **Follow Recommendations**
   - Use suggested resources
   - Implement recommended tips
   - Monitor improvements

4. **Balance Study & Interest**
   - Study time should match interest
   - High interest needs commitment
   - Balance prevents burnout

---

## 🚀 Getting Maximum Value

### **Week 1:**
- Take initial assessment
- Get recommendations
- Explore resources

### **Week 2-4:**
- Implement recommendations
- Follow learning plan
- Use resources actively

### **Month 2:**
- Take another assessment
- Review progress
- Adjust strategy

### **Ongoing:**
- Regular assessments
- Track trends
- Continuous improvement

---

## 📞 Technical Support

### **Browser Compatibility**
- ✅ Chrome (Recommended)
- ✅ Firefox
- ✅ Edge
- ✅ Safari

### **System Requirements**
- Python 3.8+
- 4GB RAM minimum
- 500MB disk space
- Stable internet connection

### **Performance Notes**
- First load may take 10-15 seconds
- Subsequent loads are faster
- Model predictions take 2-5 seconds
- Charts render smoothly

---

## 🔒 Privacy & Security

- **Data Privacy**: Student data stored locally in session
- **Password Security**: Implemented in login form
- **Future Enhancement**: Database encryption
- **No External Tracking**: No third-party analytics

---

## ✨ Features at a Glance

| Feature | Module | Status |
|---------|--------|--------|
| Login/Authentication | Auth | ✅ Active |
| Student Assessment | Assessment | ✅ Active |
| AI Prediction | Assessment | ✅ Active |
| Personalized Tips | Assessment | ✅ Active |
| Progress Tracking | Progress | ✅ Active |
| Resource Library | Resources | ✅ Active |
| Profile Management | Profile | ✅ Active |
| Data Visualization | Progress | ✅ Active |
| Database Integration | Future | 🔄 Planned |
| Mobile App | Future | 🔄 Planned |

---

## 📞 Questions?

Refer to:
1. This User Guide
2. README.md in project folder
3. Code comments in app.py
4. Streamlit documentation: https://docs.streamlit.io

---

**Version**: 1.0.0  
**Last Updated**: March 17, 2026  
**Status**: ✅ Live and Running

🎓 **Happy Learning!**
