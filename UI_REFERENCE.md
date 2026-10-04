# 📱 UI Components Reference Guide

## Navigation Structure

```
┌──────────────────────────────────────────────────┐
│         LOGIN PAGE (If not authenticated)         │
├──────────────────────────────────────────────────┤
│  🎓 AI Student Learning Path Advisor             │
│                                                  │
│  Email: [____________]                           │
│  Password: [____________]                        │
│                                                  │
│  [🔐 Login]  [📝 Sign Up]                        │
└──────────────────────────────────────────────────┘
                        ↓
┌──────────────────────────────────────────────────┐
│            MAIN APPLICATION (After Login)        │
├──────────────────────────────────────────────────┤
│                                                  │
│  ┌────────────────┬──────────────────────────┐  │
│  │ SIDEBAR        │  MAIN CONTENT            │  │
│  │                │                          │  │
│  │ 🗺️ Navigation │  [Page Content Here]     │  │
│  │ ─────────────  │                          │  │
│  │ 🏠 Home        │                          │  │
│  │ 📝 Assessment  │                          │  │
│  │ 📈 Progress    │                          │  │
│  │ 📚 Resources   │                          │  │
│  │ 👤 Profile     │                          │  │
│  │                │                          │  │
│  │ ─────────────  │                          │  │
│  │ 👤 [Username]  │                          │  │
│  │ 📧 [Email]     │                          │  │
│  │                │                          │  │
│  │ [🚪 Logout]    │                          │  │
│  └────────────────┴──────────────────────────┘  │
└──────────────────────────────────────────────────┘
```

---

## 🏠 Home Page Layout

```
┌────────────────────────────────────────────────────┐
│     🎓 AI Student Learning Path Advisor            │
├────────────────────────────────────────────────────┤
│ 👋 Welcome, [Name]!                                │
│ This system analyzes your learning patterns...     │
│                                    📊 17-Mar-2026  │
├────────────────────────────────────────────────────┤
│ ✨ KEY FEATURES                                    │
│ ┌──────────────┐  ┌──────────────┐  ┌──────────┐ │
│ │ 🤖 AI        │  │ 📈 Personalized│ │ 📊      │ │
│ │ Analysis     │  │ Path          │ │ Progress│ │
│ └──────────────┘  └──────────────┘  └──────────┘ │
├────────────────────────────────────────────────────┤
│ 📈 QUICK STATS                                     │
│ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐      │
│ │📚 12   │ │📊 78.5 │ │⏱ 2.3h │ │🎯 Adv  │      │
│ │Assess  │ │Avg Mrk │ │Avg Tim│ │Latest  │      │
│ └────────┘ └────────┘ └────────┘ └────────┘      │
└────────────────────────────────────────────────────┘
```

---

## 📝 Assessment Page Layout

```
┌────────────────────────────────────────────────────┐
│ 📝 STUDENT ASSESSMENT                              │
├────────────────────────────────────────────────────┤
│                                                    │
│  👤 Student Info         │ 📊 Performance Metrics │
│  ─────────────────────   │ ──────────────────────│
│  Name: [________]        │ Marks: [====○====]    │
│  Roll: [________]        │ Interest: [Low▼]      │
│  Subject: [Data Sci▼]    │ Study Time: [2.0 h]   │
│                          │                      │
├────────────────────────────────────────────────────┤
│ 📌 ASSESSMENT SUMMARY                              │
│ ┌──────────┐  ┌──────────┐  ┌──────────┐         │
│ │📊 78     │  │🔥 High   │  │⏱ 2.0h    │         │
│ │Marks     │  │Interest  │  │Study Time │         │
│ └──────────┘  └──────────┘  └──────────┘         │
│                                                    │
│ [🤖 Generate Learning Path Recommendation]        │
└────────────────────────────────────────────────────┘
```

---

## 🎯 Results Page Layout

```
┌────────────────────────────────────────────────────┐
│ 🎯 ASSESSMENT RESULTS                              │
├────────────────────────────────────────────────────┤
│                                                    │
│ ┌──────────┐  ┌──────────┐  ┌──────────┐         │
│ │👤 John   │  │🟢 Advanced│ │📈 89.5%  │         │
│ │Student   │  │Level      │ │Confidence│         │
│ └──────────┘  └──────────┘  └──────────┘         │
│                                                    │
│ ███████████████████ 89.5%                         │
│                                                    │
├────────────────────────────────────────────────────┤
│ 🟢 PERSONALIZED LEARNING PATH                     │
│                                                    │
│ 📌 RECOMMENDED ACTIONS:    📚 SUGGESTED RESOURCES:│
│ 1. 🚀 Work on real-world   • GitHub             │
│    industry projects       • Research Papers     │
│ 2. 🔬 Explore advanced     • Industry           │
│    topics                    Internships        │
│ 3. 📊 Contribute to        • Advanced Courses   │
│    open-source            • Mentorship         │
│ 4. 🎓 Aim for mastery     •                    │
│ 5. 💼 Build portfolio     •                    │
│ 6. 🏆 Advanced certs      •                    │
│                                                    │
├────────────────────────────────────────────────────┤
│ 📊 LEARNING PROFILE VISUALIZATION                 │
│ ┌──────────────────────┐  ┌──────────────────────┐│
│ │ Marks  Interest Time  │  │ Confidence Gauge     ││
│ │ │   │   │   │   │   │  │ ████████████ 89.5%  ││
│ │ │ 78│ 3 │ 2 │   │   │  │                      ││
│ │ └───┴───┴───┘   │   │  │ Reference: 80%       ││
│ └──────────────────────┘  └──────────────────────┘│
│                                                    │
│ ✅ Assessment completed! Level: Advanced          │
└────────────────────────────────────────────────────┘
```

---

## 📈 Progress Page Layout

```
┌────────────────────────────────────────────────────┐
│ 📈 PROGRESS TRACKING                               │
├────────────────────────────────────────────────────┤
│                                                    │
│ 📊 ASSESSMENT HISTORY                              │
│ ┌─────────────────────────────────────────────┐   │
│ │ Name  | Marks | Level | Interest | Date    │   │
│ ├─────────────────────────────────────────────┤   │
│ │ John  │ 65    │ Inter │ Medium   │ 15-Mar  │   │
│ │ John  │ 78    │ Advan │ High     │ 16-Mar  │   │
│ │ John  │ 82    │ Advan │ High     │ 17-Mar  │   │
│ └─────────────────────────────────────────────┘   │
│                                                    │
├────────────────────────────────────────────────────┤
│ 📉 PERFORMANCE TRENDS                              │
│                                                    │
│ Marks Progression      │ Study Time Progression    │
│ ┌───────────────────┐  │ ┌───────────────────┐   │
│ │ 85 ╱─────         │  │ │ 3.0 ╱─────        │   │
│ │ 78    ╱─────      │  │ │ 2.5   ╱─────     │   │
│ │ 65 ─╱            │  │ │ 2.0 ─╱           │   │
│ │ #1  #2  #3       │  │ │ #1  #2  #3      │   │
│ └───────────────────┘  │ └───────────────────┘   │
│                                                    │
│ Level Distribution     │ Interest Distribution    │
│ ┌───────────────────┐  │ ┌───────────────────┐   │
│ │ ██ Beginner  (0)  │  │ │ Medium 33%        │   │
│ │ ██ Intermediate(1)│  │ │ ████  High 67%    │   │
│ │ ██ Advanced   (2) │  │ │                   │   │
│ └───────────────────┘  │ └───────────────────┘   │
└────────────────────────────────────────────────────┘
```

---

## 📚 Resources Page Layout

```
┌────────────────────────────────────────────────────┐
│ 📚 LEARNING RESOURCES                              │
├────────────────────────────────────────────────────┤
│                                                    │
│ Select Subject: [Data Science ▼]                  │
│                                                    │
├────────────────────────────────────────────────────┤
│ 📖 Resources for Data Science                      │
│                                                    │
│  📕 BOOKS              │  🎓 ONLINE COURSES      │
│  ──────────────────    │  ──────────────────    │
│  • Python for Data     │  • Coursera - DS       │
│    Analysis            │  • Udacity Scientist   │
│  • Data Science from   │  • DataCamp            │
│    Scratch             │                        │
│  • Hands-On ML         │  🌐 WEBSITES           │
│                        │  ──────────────────    │
│  🌐 WEBSITES           │  • Kaggle              │
│  ──────────────────    │  • Analytics Vidhya    │
│  • Kaggle              │  • Towards Data Sci    │
│  • Analytics Vidhya    │                        │
│  • Medium              │  📹 YOUTUBE CHANNELS   │
│                        │  ──────────────────    │
│  📹 YOUTUBE CHANNELS   │  • StatQuest           │
│  ──────────────────    │  • Krish Naik          │
│  • StatQuest           │  • Code Basics         │
│  • Krish Naik          │                        │
│  • Code Basics         │                        │
│                                                    │
└────────────────────────────────────────────────────┘
```

---

## 👤 Profile Page Layout

```
┌────────────────────────────────────────────────────┐
│ 👤 MY PROFILE                                      │
├────────────────────────────────────────────────────┤
│                                                    │
│ ACCOUNT INFORMATION    │ QUICK LINKS             │
│ ──────────────────    │ ───────────────         │
│ Email: john@col.edu   │ • 📝 Take Assessment   │
│ Name: john            │ • 📈 View Progress     │
│ Member Since: Mar 26  │ • 📚 Learning Resources│
│                       │ • ⚙️ Settings          │
│ ──────────────────    │                         │
│ STATISTICS            │                         │
│ ──────────────────    │                         │
│ Total Assessments: 3  │                         │
│ Avg Marks: 75.0/100   │                         │
│ Current Level: Adv    │                         │
│                                                    │
└────────────────────────────────────────────────────┘
```

---

## 🎨 Color Coding Reference

```
🔴 RED (#ff6b6b)
   └─ Beginner Level
      └─ Needs improvement

🟡 YELLOW (#ffd93d)
   └─ Intermediate Level
      └─ Good progress

🟢 GREEN (#6bcf7f)
   └─ Advanced Level
      └─ Excellent

🔵 BLUE (#667eea, #764ba2)
   └─ Primary colors
   └─ Headers, buttons, primary info
```

---

## 📱 Button Guide

```
LOGIN BUTTONS:
[🔐 Login]  - Primary login action
[📝 Sign Up] - Future signup

ASSESSMENT BUTTONS:
[🤖 Generate Learning Path Recommendation] - Main action

PROGRESS BUTTONS:
(No action buttons, display-only)

PROFILE BUTTONS:
(No action buttons, display-only)

SIDEBAR BUTTONS:
[🚪 Logout] - Exit application
```

---

## 📊 Icon Legend

```
🎓 Education / System Title
🔐 Security / Login
👤 User / Profile
📧 Email / Contact
🔑 Password
📝 Assessment / Writing
📊 Metrics / Charts / Marks
📈 Progress / Analytics
📉 Trends / Decline
🎯 Goals / Results
🔥 Interest / Energy
⏱  Time / Duration
💡 Tips / Insights
🤖 AI / Machine Learning
📚 Resources / Learning
📕 Books
📹 Video / YouTube
🌐 Website / Internet
🎓 Courses / Education
✅ Success / Checkmark
❌ Error / Close
ℹ️ Information
⚙️ Settings
🚪 Logout / Exit
🔄 Refresh / Reload
═══ Divider / Separator
─── Subheader
```

---

## 🎯 User Journey Map

```
START
  │
  ├─→ LOGIN PAGE
  │   │
  │   ├─→ [Invalid] ─→ Error Message ─→ Retry
  │   │
  │   └─→ [Valid] ─→ Create Session
  │
  ├─→ DASHBOARD
  │   │
  │   └─→ Choose Action
  │       │
  │       ├─→ ASSESSMENT
  │       │   ├─→ Fill Form
  │       │   ├─→ AI Prediction
  │       │   └─→ View Results
  │       │
  │       ├─→ PROGRESS
  │       │   ├─→ View History
  │       │   └─→ Analyze Trends
  │       │
  │       ├─→ RESOURCES
  │       │   ├─→ Select Subject
  │       │   └─→ Browse Materials
  │       │
  │       ├─→ PROFILE
  │       │   ├─→ View Account Info
  │       │   └─→ Check Statistics
  │       │
  │       └─→ LOGOUT
  │           │
  │           └─→ Return to Login

END
```

---

## 🎬 Interaction Flow

```
User Action → Streamlit Widget → Python Function → Data Processing
    ↑                                               │
    └─────────────── Page Refresh ←─────────────────┘
```

---

## 📐 Layout Dimensions

```
FULL PAGE: 100% width
├─ SIDEBAR: 300px (fixed)
└─ MAIN: 100% - 300px (fluid)

CONTENT GRIDS:
├─ 1 Column: Full width
├─ 2 Columns: 50% | 50%
├─ 3 Columns: 33% | 33% | 33%
└─ Custom: Adjustable

METRICS:
├─ Width: 200px each
├─ Height: 100px
└─ Spacing: 10px

CHARTS:
├─ Width: Container width
├─ Height: 400px
└─ Padding: 20px
```

---

## 🖥️ Responsive Design Notes

```
Desktop (1920+):
└─ Full layout with all features
└─ Sidebar visible
└─ 3-column layouts possible

Tablet (1024-1920):
└─ 2-column layouts
└─ Sidebar collapsible
└─ Good readability

Mobile (< 1024):
⚠️ Not optimized
└─ Single column
└─ Features still accessible
```

---

**UI Components Reference v1.0**  
Last Updated: March 17, 2026

This guide provides visual reference for all UI components in the system.
