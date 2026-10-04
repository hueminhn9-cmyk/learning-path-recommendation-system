# AI Student Learning Advisor - Mini Project

A simplified AI-powered student learning path recommendation system.

## Features

- **Login System**: Simple authentication
- **AI Assessment**: Student performance evaluation using machine learning
- **Learning Recommendations**: Personalized study path suggestions
- **Visual Analytics**: Basic charts showing learning profile

## Technology Stack

- **Frontend**: Streamlit
- **AI/ML**: TensorFlow, Scikit-learn
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib

## Installation

1. Install dependencies:
```bash
pip install -r mini_requirements.txt
```

2. Run the application:
```bash
streamlit run mini_app.py
```

## Project Structure

```
mini_project/
├── mini_app.py          # Main Streamlit application
├── mini_requirements.txt # Python dependencies
├── model/              # Trained AI models
│   ├── student_model.h5
│   ├── scaler.pkl
│   └── level_map.pkl
└── dataset/
    └── students.csv    # Sample data
```

## Usage

1. **Login** with any email and password
2. **Take Assessment** by filling student information and performance metrics
3. **View Results** with AI-generated learning recommendations and visualizations

## AI Model

The system uses a neural network trained on student data to predict learning levels:
- **Beginner**: Basic concepts and fundamentals
- **Intermediate**: Practical applications and problem-solving
- **Advanced**: Complex projects and specialization

## Mini Project Scope

This is a focused mini project demonstrating:
- Machine learning integration in web applications
- Student performance analysis
- Personalized recommendation systems
- Data visualization for educational insights