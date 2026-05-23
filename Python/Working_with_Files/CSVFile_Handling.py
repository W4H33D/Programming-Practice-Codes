import csv          # Standard CSV Library

# Reading CSV Files
with open("CSVs/student_data.csv", mode="r", newline="") as file:        # `newline` helps the csv module to handle line endings correctly
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row

    for row in reader:              # i.e, ['Alice', '25', '90']
        name, age, score = row      # [Sequence Unpacking Used]: Unpacks the row into separate variables
        print(f"{name} is {age} years old and scored {score}.")

# Writing CSV Files
data = [
    ["Name", "Age", "Score"],
    ["Ali", 25, 90],
    ["Hassan", 20, 75],
    ["Usman", 21, 81]
]

with open("CSVs/my_student_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading Back The New CSV File
with open("CSVs/my_student_data.csv", mode="r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        name, age, score = row
        print(f"{name} is {age} years old and scored {score}.")
