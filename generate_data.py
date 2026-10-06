import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
n_rows = 10000

subjects = [
    "Machine Learning", 
    "Data Science", 
    "Cybersecurity", 
    "Web Development", 
    "Cloud Computing", 
    "Artificial Intelligence",
    "Mobile App Development",
    "Software Engineering",
    "Database Systems",
    "Computer Networks"
]

subject_data = np.random.choice(subjects, n_rows)
marks = np.random.randint(0, 101, n_rows)

interest_levels = []
interest_nums = []
time_spent = []

for m in marks:
    noise_interest = np.random.choice([-1, 0, 1], p=[0.1, 0.8, 0.1])
    noise_time = np.random.uniform(-0.8, 0.8)
    
    if m <= 45:
        base_interest = 1
        base_time = 1.5
    elif m <= 75:
        base_interest = 2
        base_time = 3.5
    else:
        base_interest = 3
        base_time = 6.0
        
    i_num = int(np.clip(base_interest + noise_interest, 1, 3))
    t_val = round(float(np.clip(base_time + noise_time, 0.5, 10.0)), 1)
    i_str = {1: "Low", 2: "Medium", 3: "High"}[i_num]
    
    interest_nums.append(i_num)
    interest_levels.append(i_str)
    time_spent.append(t_val)

df = pd.DataFrame({
    'Student_ID': [f"SV{i+1000:04d}" for i in range(n_rows)],
    'Subject': subject_data,
    'Marks': marks,
    'Interest': interest_levels,
    'Interest_Score': interest_nums,
    'Time_Spent_Hours': time_spent
})

df.to_csv('dataset/students.csv', index=False)
print("Generated 10,000 rows of structured synthetic data.")

