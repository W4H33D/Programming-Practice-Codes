def cleaning_records(records):

    # --- Original Output ---
    print("[+] Showing Original Raw Records\n")
    for i, rec in enumerate(records):
        print(f"|    {i+1}. {rec}")
    print(f"↳ Total {i+1} Records Found.")
    print("---" * 50)

    # --- Cleaning Process 1: Removing None Values ---
    print("\n[Cleaning Process 1] Removing None Values\n")
    records = [
        rec for rec in records
        if all(key is not None and value is not None for key, value in rec.items())
    ]
    for i, rec in enumerate(records):
        print(f"|    {i+1}. {rec}")

    # --- Cleaning Process 2: Removing Extra Spaces ---
    print("\n[Cleaning Process 2] Removing Extra Spaces\n")
    records = [
        {k.strip().replace(' ', '_'): v.strip() for k, v in rec.items()}
        for rec in records
    ]
    for i, rec in enumerate(records):
        print(f"|    {i+1}. {rec}")

    # --- Cleaning Process 3: Removing Exact Duplicates ---
    print("\n[Cleaning Process 3] Removing Exact Duplicates\n")
    seen = set()
    deduped = []
    for rec in records:
        key = tuple(rec.items())
        if key not in seen:
            seen.add(key)
            deduped.append(rec)
    records = deduped
    del deduped, seen           # explicitly free helper structures
    for i, rec in enumerate(records):
        print(f"|    {i+1}. {rec}")

    # --- Cleaning Process 4: Standardization (Final Output) ---
    print("\n[Cleaning Process 4] Standardization — Final Output\n")
    records = [
        {k.lower(): v.lower() for k, v in rec.items()}
        for rec in records
    ]
    for i, rec in enumerate(records):
        print(f"|    {i+1}. {rec}")
    print(f"\n↳ {len(records)} Clean Records After Full Pipeline.")
    return records

def validate_data(dataset, valueToCheck, low_limit, high_limit):

    def to_number(value):
        if isinstance(value, (int, float)):   # already numeric, use directly
            return value
        if isinstance(value, str):            # string, attempt conversion
            try:
                return float(value)
            except ValueError:
                return None                   # unconvertible string e.g. 'N/A'
        return None                           # any other type e.g. list, dict

    out_of_range = []
    skipped = []

    for i, rec in enumerate(dataset):
        raw = rec.get(valueToCheck)
        val = to_number(raw)
        if val is None:
            skipped.append((i, rec))
        elif val < low_limit or val > high_limit:
            out_of_range.append((i, rec))

    print(f"\n[!] Out-of-Range Records for '{valueToCheck}' (valid: {low_limit}–{high_limit})\n")
    if out_of_range:
        for i, rec in out_of_range:
            print(f"|    [index {i}] {rec}")
    else:
        print("|    No out-of-range records found.")
    print(f"↳ {len(out_of_range)} Record(s) Flagged.")

    if skipped:
        print(f"\n[!] {len(skipped)} Record(s) Skipped — could not read '{valueToCheck}' as a number.")
        for i, rec in skipped:
            print(f"|    [index {i}] {rec}")

    return out_of_range

def replace_invalid_records(dataset, recordIndex, invalidRecord, valueToReplaceWith=None):
    for recordIndex in recordIndex:
        record = dataset[recordIndex]
        invalid_record = record.get(invalidRecord)
        if invalid_record is not valueToReplaceWith:
            print(f"FLAGGING invalid Record [index: {recordIndex}] → {invalidRecord}: {invalid_record}")
            record[invalidRecord] = valueToReplaceWith
    print(f"\n--- After Marking Invalid Values as {valueToReplaceWith} ---")
    for rec in dataset:
        print(rec)

attendance_records = [
    {'Employee_id': ' EMP001', 'employee_name': 'Alice', 'attendance_date': '2026-05-01', 'status': 'Present', 'hours_worked': '8'},
    {'employee_id': 'emp001', 'employee_name': ' Alice', 'attendance_date': '2026-05-01', 'status': 'present', 'hours_worked': '8'},
    {'Employee ID': 'EMP001 ', 'employee_name': 'alice ', 'attendance_date': '2026-05-01', 'status': 'Present', 'hours_worked': '8'},
    {'employee_id': 'EMP002', 'employee_name': 'Bob',   'attendance_date': '2026-05-01', 'status': 'Absent',  'hours_worked': '-1'},
    {'employee_id': 'EMP003', 'employee_name': 'Eve',   'attendance_date': '2026-05-03', 'status': 'absent', 'hours_worked': '9'},
    {'employee_id': 'EMP004', 'employee_name': 'Frank', 'attendance_date': '2026-05-03', 'status': 'Present', 'hours_worked': '25'},
    {'employee_id': 'EMP005', 'employee_name': 'Grace', 'attendance_date': '2026-05-04', 'status': 'Present', 'hours_worked': '7.5'},
]

attendance_data = [
    {'employee_id': 'EMP001', 'project_code': 'PROJ-A', 'hours_worked': "8"},
    {'employee_id': 'EMP002', 'project_code': 'PROJ-A', 'hours_worked': "-1"},
    {'employee_id': 'EMP003', 'project_code': 'PROJ-B', 'hours_worked': "9"},
    {'employee_id': 'EMP004', 'project_code': 'PROJ-A', 'hours_worked': "25"},
    {'employee_id': 'EMP005', 'project_code': 'PROJ-B', 'hours_worked': "7.5"},
    {'employee_id': 'EMP006', 'project_code': 'PROJ-C', 'hours_worked': None},
    {'employee_id': 'EMP007', 'project_code': None, 'hours_worked': "8"},
]

#stand_record = cleaning_records(attendance_records)
invalid_rec = validate_data(attendance_data, 'hours_worked', 0 , 16)
replace_invalid_records(attendance_data, [1, 3, 5],'hours_worked', None)
