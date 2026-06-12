### TL;DR

In this project, you will act as a Junior Data Analyst reviewing student performance data from a short academic program.
You will

- Clean a missing value
- Calculate averages
- Summarize categories
- Use NumPy for statistics
- Apply conditional filtering
- Detect an outlier
- Write a short EDA-style summary.

### Project: The Student Performance Review

**Scenario**

You are working as a Junior Data Analyst for a small training center. The academic team has collected student performance records from a short program and wants a first analytical review. The dataset contains each student’s department, two quiz scores, and a final project score. However, one quiz value is missing, and the team wants a quick summary of performance before preparing a formal report.

Your job is to:

- **clean the data**
- **calculate useful statistics**
- **identify important subgroups**
- **check for possible outliers**
- **produce a short exploratory summary**.

The records are already provided in Python as a list of dictionaries.

```python
student_records = [
    {'student_id': 'P01', 'department': 'Data', 'quiz_1': 82, 'quiz_2': 85, 'final_project': 88},
    {'student_id': 'P02', 'department': 'Web', 'quiz_1': 91, 'quiz_2': 89, 'final_project': 93},
    {'student_id': 'P03', 'department': 'Data', 'quiz_1': 76, 'quiz_2': None, 'final_project': 79},
    {'student_id': 'P04', 'department': 'AI', 'quiz_1': 97, 'quiz_2': 95, 'final_project': 99},
    {'student_id': 'P05', 'department': 'Web', 'quiz_1': 68, 'quiz_2': 72, 'final_project': 70},
    {'student_id': 'P06', 'department': 'Data', 'quiz_1': 60, 'quiz_2': 64, 'final_project': 58}
]
```

The Solution Of this lab is found in `solution.py` file. However for better result try to solve each problem at your own.
