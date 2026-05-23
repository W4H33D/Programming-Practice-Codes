try:
    with open("CSVs/sales_data.csv", 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip().split(',')
            print(repr(data))
except FileNotFoundError:
    print("File Doesn't Exits -- Check Your Path or Name")
except Exception as e:
    print(f"Something Want Wrong...\nDebug : {e}")
else:
    pass
finally:
    pass
