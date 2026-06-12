student_data = [
    {'student_id': 'S01', 'major': 'Physics', 'exam_1': 85, 'exam_2': 88, 'final_project': 92},
    {'student_id': 'S02', 'major': 'Chemistry', 'exam_1': 91, 'exam_2': 89, 'final_project': 94},
    {'student_id': 'S03', 'major': 'Physics', 'exam_1': 78, 'exam_2': 82, 'final_project': 80},
    {'student_id': 'S04', 'major': 'Engineering', 'exam_1': 95, 'exam_2': 98, 'final_project': 99},
    {'student_id': 'S05', 'major': 'Chemistry', 'exam_1': 88, 'exam_2': None, 'final_project': 91},
    {'student_id': 'S06', 'major': 'Physics', 'exam_1': 65, 'exam_2': 70, 'final_project': 72}
]

#for student in student_data
#    print(student)

cleaned_data = []
missing_value_count = 0

for student in student_data:
    if student['exam_2'] is None:
        student['exam_2'] = student['exam_1']
        missing_value_count += 1

    total_score = student['exam_1'] + student['exam_2'] + student['final_project']
    student['average_score'] = round(total_score / 3, 2)

    cleaned_data.append(student)

print("Initial Inspection & Preparation:")
print(f" [+] Found and imputed {missing_value_count} missing value(s).")
print(" [+] Added 'average_score' to each record.")

for data_i in cleaned_data:
    print(f" {data_i}")

major_counts = {}

for student in cleaned_data:
    major = student['major']
    if major not in major_counts:
        major_counts[major] = 0
    major_counts[major] += 1

print("Student Count per Major:")
for major, count in major_counts.items():
    print(f" - {major}: {count} student(s)")

sorted_by_score = sorted(cleaned_data, key=lambda s: s['average_score'], reverse=True)

print("Top 3 Students by Average Score:")
for student in sorted_by_score[:3]:
    print(f" - {student['student_id']} (Major: {student['major']}): {student['average_score']}")

physics_students = []

for student in cleaned_data:
    if student['major'] == 'Physics':
        physics_students.append(student)

print("Analysis of Physics Majors Only:")
for student in physics_students:
    print(f" - {student['student_id']}: {student['average_score']}")

import numpy as np

project_scores = [s['final_project'] for s in cleaned_data]

mean_score = np.mean(project_scores)
std_dev = np.std(project_scores)
outlier_threshold = 1.5

print(f"Outlier Detection in Final Project Scores (Mean={mean_score:.2f}, StdDev={std_dev:.2f}):")

outliers = []

for student in cleaned_data:
    score = student['final_project']
    z_score = (score - mean_score) / std_dev

    if abs(z_score) > outlier_threshold:
        outliers.append(student)
        print(f"- Found Outlier: Student {student['student_id']} with score {score} (Z-score: {z_score:.2f})")

if not outliers:
    print("- No significant outliers found based on the threshold.")

exam_1_scores = [s['exam_1'] for s in cleaned_data]
final_project_scores = [s['final_project'] for s in cleaned_data]

correlation_matrix = np.corrcoef(exam_1_scores, final_project_scores)
correlation_coefficient = correlation_matrix[0, 1]

print("Correlation between Exam 1 and Final Project:")
print(f"Correlation Coefficient: {correlation_coefficient:.4f}")

if correlation_coefficient > 0.7:
    print("Interpretation: Strong positive correlation.")
elif correlation_coefficient > 0.4:
    print("Interpretation: Moderate positive correlation.")
elif correlation_coefficient < -0.4:
    print("Interpretation: Moderate negative correlation.")
else:
    print("Interpretation: Weak or no correlation.")