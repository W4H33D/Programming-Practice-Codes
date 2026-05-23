import os

file_path = "CSVs/feedback_students.txt"
if os.path.exists(file_path):           # Checks If the file exits or not
    print("File exists. Ready to load.")
else:
    print("File does not exist. Please check the path.")
    exit(1)

# open("feedback_students.txt", 'r', 'utf-8')       #Syntax: open(file_path, mode, encoding)
with open(file_path, 'r', encoding='utf-8') as file:   # safe way to open a file
    # Working With File Code here
    lines = file.readlines()        # readlines() method read every line of the file.
    for l in lines:                 # We loop on each line one by one
        print(l.strip())            # .strip() method removes spaces, tabs, and newline characters from beginning and end
                                    # Note readlines() method good for small file however it doesn't fit for
                                    # Large files because it will take too much memory. The best way to read is:

print("\n== Best Way To Read Files ==\n")
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())

print("\n== Error Handling In File Operations ==\n")
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f"File ({file_path}) Doesn't Exits.")
except Exception as e:
    print(f"Error Occurred: {e}")
else:
    # Execute When Try Block Run Without Any Error
    print("Log   :   File Successfully Read")
finally:
    # Runs For sure
    print("Log   :   Try BLock Is Ended")