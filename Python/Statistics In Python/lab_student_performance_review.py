import math
import numpy as np
from nbclient.exceptions import timeout_err_msg

student_records = [
    {'student_id': 'P01', 'department': 'Data', 'quiz_1': 82, 'quiz_2': 85, 'final_project': 88},
    {'student_id': 'P02', 'department': 'Web', 'quiz_1': 91, 'quiz_2': 89, 'final_project': 93},
    {'student_id': 'P03', 'department': 'Data', 'quiz_1': 76, 'quiz_2': None, 'final_project': 79},
    {'student_id': 'P04', 'department': 'AI', 'quiz_1': 97, 'quiz_2': 95, 'final_project': 99},
    {'student_id': 'P05', 'department': 'Web', 'quiz_1': 68, 'quiz_2': 72, 'final_project': 70},
    {'student_id': 'P06', 'department': 'Data', 'quiz_1': 60, 'quiz_2': 64, 'final_project': 58}
]

cleaned_records = []
marks_record = []
student_count = {}
missing_values = 0


for i, record in enumerate(student_records):
    if record['quiz_2'] == None:
        record['quiz_2'] = record['quiz_1']
        missing_values += 1
    cleaned_records.append(record)
    marks_record.append([ record['quiz_1'], record['quiz_2'], record['final_project'] ])
    record['Average'] = round(float(np.mean(marks_record[i])), 2)

for student in cleaned_records:
    dept = student['department']
    if dept not in student_count:
        student_count[dept] = 0
    student_count[dept] += 1


print(f"Cleaned Student Records\n" +
    f"".join(f"   {i} {record}\n" for i, record in enumerate(cleaned_records))
    + f"\n Total Student Per Department"
    + f"\n   {'Department':<15} {'Total Students'}\n"
    + f"   {'-'*30}\n" + "".join(f"   {dept:<15} {count}\n" for dept, count in student_count.items())
)

sorted_by_score = sorted(cleaned_records, key=lambda s: s['Average'], reverse=True)
print(f"Top 3 Most Scored Departments"
    f"\n   {'Student ID':<15} {'Department':<15} {'Average':<15}\n"
    f"   {'-'*40}"
)
for student in sorted_by_score[:3]:
    print(f"   {student['student_id']:<15} {student['department']:<15} {student['Average']:<15}")

data_dept = []

for record in cleaned_records:
    if record['department'] == 'Data':
        data_dept.append(record)

print(f"\nData Department Student Records"
      + f"\n{'-'*40}\n"
      + f"".join(f"{i} {record}" "\n" for i, record in enumerate(data_dept))
      )

avg_marks = []
for record in cleaned_records:
   avg_marks.append(record['Average'])

cal_mean = np.mean(avg_marks)
cal_median = np.median(avg_marks)
cal_total = np.sum(avg_marks)
cal_std = np.std(avg_marks)

print(
    f"Statistics Summary\n"
    + f"".join(f"   Mean {cal_mean}\n   Median {cal_median}\n   Total {cal_total}\n   STD {cal_std}")
    )

strong_students = []

for student in cleaned_records:
    if student['Average'] >= 80:
        strong_students.append(student)

print("Students with average >= 80:")
for student in strong_students:
    print(student['student_id'])

print("\nPerformance labels:")
for student in cleaned_records:
    if student['Average'] >= 90:
        label = "Strong"
    elif student['Average'] >= 75:
        label = "Satisfactory"
    else:
        label = "Needs Support"
    print(f"   {student['student_id']} is {label}")

final_scores = [student['final_project'] for student in cleaned_records]

mean_score = np.mean(final_scores)
std_dev = np.std(final_scores)

print(f"Mean={mean_score:.2f}, StdDev={std_dev:.2f}")

for student in cleaned_records:
    z_score = (student['final_project'] - mean_score) / std_dev
    if abs(z_score) > 1.5:
        print("Possible outlier:", student['student_id'], student['final_project'], round(z_score, 2))

quiz_1_scores = [student['quiz_1'] for student in cleaned_records]
final_scores = [student['final_project'] for student in cleaned_records]

correlation_matrix = np.corrcoef(quiz_1_scores, final_scores)
correlation = correlation_matrix[0, 1]

print("Correlation:", round(correlation, 4))

print("\nEDA Summary:")
print(f"- Missing values fixed: {missing_values}")
print(f"- Department counts: {f"".join({f"{dept} {count}," for dept, count in student_count.items()})})")
print(f"- Top performer: {sorted_by_score[0]['student_id']} with average {sorted_by_score[0]['Average']}")
print(f"- Correlation between quiz_1 and final_project: {round(correlation, 4)}")
print("- Review any flagged outliers carefully before drawing conclusions.")
