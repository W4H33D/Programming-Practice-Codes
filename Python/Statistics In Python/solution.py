import math
import numpy as np

student_records = [
    {'student_id': 'P01', 'department': 'Data', 'quiz_1': 82, 'quiz_2': 85, 'final_project': 88},
    {'student_id': 'P02', 'department': 'Web', 'quiz_1': 91, 'quiz_2': 89, 'final_project': 93},
    {'student_id': 'P03', 'department': 'Data', 'quiz_1': 76, 'quiz_2': None, 'final_project': 79},
    {'student_id': 'P04', 'department': 'AI', 'quiz_1': 97, 'quiz_2': 95, 'final_project': 99},
    {'student_id': 'P05', 'department': 'Web', 'quiz_1': 68, 'quiz_2': 72, 'final_project': 70},
    {'student_id': 'P06', 'department': 'Data', 'quiz_1': 60, 'quiz_2': 64, 'final_project': 58}
]

# Write your solution here
cleaned_data = []
missing_count = 0

for student in student_records:
    if student['quiz_2'] is None:
        student['quiz_2'] = student['quiz_1']
        missing_count += 1
    cleaned_data.append(student)

print(f"Missing values imputed: {missing_count}")

for student in cleaned_data:
    total = student['quiz_1'] + student['quiz_2'] + student['final_project']
    student['average_score'] = round(total / 3, 2)

for student in cleaned_data:
    print(student['student_id'], student['average_score'])

department_counts = {}

for student in cleaned_data:
    dept = student['department']
    if dept not in department_counts:
        department_counts[dept] = 0
    department_counts[dept] += 1

print(department_counts)

sorted_students = sorted(cleaned_data, key=lambda s: s['average_score'], reverse=True)

print("Top students:")
for student in sorted_students[:3]:
    print(student['student_id'], student['average_score'])

data_students = []
for student in cleaned_data:
    if student['department'] == 'Data':
        data_students.append(student)

print("\nData department:")
for student in data_students:
    print(student['student_id'], student['average_score'])

average_scores = np.array([student['average_score'] for student in cleaned_data])

print("Mean:", np.mean(average_scores))
print("Median:", np.median(average_scores))
print("Total:", np.sum(average_scores))
print("Std Dev:", np.std(average_scores))


strong_students = []

for student in cleaned_data:
    if student['average_score'] >= 80:
        strong_students.append(student)

print("Students with average >= 80:")
for student in strong_students:
    print(student['student_id'])

print("\nPerformance labels:")
for student in cleaned_data:
    if student['average_score'] >= 90:
        label = "Strong"
    elif student['average_score'] >= 75:
        label = "Satisfactory"
    else:
        label = "Needs Support"
    print(student['student_id'], label)

    final_scores = [student['final_project'] for student in cleaned_data]

mean_score = np.mean(final_scores)
std_dev = np.std(final_scores)

print(f"Mean={mean_score:.2f}, StdDev={std_dev:.2f}")

for student in cleaned_data:
    z_score = (student['final_project'] - mean_score) / std_dev
    if abs(z_score) > 1.5:
        print("Possible outlier:", student['student_id'], student['final_project'], round(z_score, 2))

quiz_1_scores = [student['quiz_1'] for student in cleaned_data]
final_scores = [student['final_project'] for student in cleaned_data]

correlation_matrix = np.corrcoef(quiz_1_scores, final_scores)
correlation = correlation_matrix[0, 1]

print("Correlation:", round(correlation, 4))

print("\nEDA Summary:")
print(f"- Missing values fixed: {missing_count}")
print(f"- Department counts: {department_counts}")
print(f"- Top performer: {sorted_students[0]['student_id']} with average {sorted_students[0]['average_score']}")
print(f"- Correlation between quiz_1 and final_project: {round(correlation, 4)}")
print("- Review any flagged outliers carefully before drawing conclusions.")
