# --- RAW DIRTY INPUT ---
raw_id     = "STU-2024-099"
raw_name   = "mARIA gARCIA"
raw_age    = "20"
clean_name = raw_name.title()
compact_id = "STU099"


prefix = raw_id[0:3]   # 'STU'        — characters at 0, 1, 2
year   = raw_id[4:8]   # '2024'       — characters at 4, 5, 6, 7
number = raw_id[9:]    # '099'        — from index 9 to the end
dept   = raw_id[:3]    # 'STU'        — same as [0:3], start omitted
year_extracted = raw_id[4:8]
first_name = raw_name[0:5]     # 'mARIA'
id_number = raw_id[9:]         # slice out '099'

id_number.isdigit()     # True
raw_age.isdigit()       # True  — "20" is all digits
"20.5".isdigit()        # False — the dot breaks it
first_name.isalpha()    # True
raw_name.isalpha()      # False — the space in the middle breaks it
compact_id.isalnum()   # True  — letters + digits only
raw_id.isalnum()       # False — hyphens are not allowed

ID_check_1 = raw_id.startswith("STU")   # True  — valid student prefix
ID_check_2 = raw_id.endswith("099")     # True  — valid serial end
raw_id_length = len(raw_id)       # 12
clean_name_length = len(clean_name)   # 11
first_hyphen_index = raw_id.find("-")  # 3

corrected_id = "ENG" + raw_id[3:] # ENG-2024-099
raw_name.lower()   # 'maria garcia'
raw_name.upper()   # 'MARIA GARCIA'
raw_name.capitalize()  # 'Maria garcia'

MIN_ID_LENGTH = 10
if len(raw_id) >= MIN_ID_LENGTH:
    print("ID length is valid.")   # 12 is greater than 10 which returns True

report = f"Student: {clean_name} | ID: {raw_id} | Enrolled: {year_extracted}"
print(report)
print(f"Name length  : {len(clean_name)}")
print(f"Valid prefix : {raw_id.startswith('STU')}")
print(f"Graduation   : {int(year_extracted) + 4}")

print("\n===== Register User =====")
# Text input — use directly or clean with a method
name_input = input("Enter student name: ")
clean_input = name_input.title()   # normalize capitalization right away
age_input = int(input("Enter student age: "))
grad_year = 2026 + (4 - (age_input - 18))
print(f"Registered as: {clean_input}")
print(f"Estimated graduation year: {grad_year}")
