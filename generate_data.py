import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
n_rows = 150

marks = np.random.randint(0, 101, n_rows)
interest_levels = []
time_spent = []

for m in marks:
    if m <= 40:
        interest = "Low"
        time = np.random.uniform(0.5, 2.0)
    elif m <= 75:
        interest = "Medium"
        time = np.random.uniform(2.1, 4.5)
    else:
        interest = "High"
        time = np.random.uniform(4.6, 8.0)
    interest_levels.append(interest)
    time_spent.append(time)

df = pd.DataFrame({
    'Student_ID': range(1, n_rows + 1),
    'Subject': 'Data Science',
    'Marks': marks,
    'Interest': interest_levels,
    'Time_Spent': time_spent
})

df.to_csv('dataset/students.csv', index=False)
print("Generated 150 rows of structured synthetic data.")
