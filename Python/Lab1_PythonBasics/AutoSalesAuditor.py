# 1. Create your raw_sales list
raw_sales = [25.50, "error", 40.00, 15.75, "missing", 100.00]

# 2-4. Define your audit_sales function
def audit_sales(sales_list):
    sales_cleaned = []
    sales_errors = []

    for index, sales_i in enumerate(raw_sales):
        try:
            sales_cleaned.append(float(sales_i))
        except (ValueError, TypeError):
            sales_errors.append((index, sales_i))

    sales_count = len(sales_cleaned)
    total_sales = sum(sales_cleaned)

    if sales_count == 0:
        average_sales = 0.0
    else:
        average_sales = total_sales / sales_count

    return {
        "cleaned_sales": sales_cleaned,
        "total_sales": total_sales,
        "average_sales": average_sales,
        "count": sales_count,
        "errors": sales_errors,
    }

# Final: Call your function with raw_sales and print the result
sales_stats = audit_sales(raw_sales)
print(f"{sales_stats['cleaned_sales'] = }\n"
      f"{sales_stats['total_sales'] = }\n"
      f"{sales_stats['average_sales'] = }\n"
      f"{sales_stats['count'] = }\n"
      f"{sales_stats['errors'] = }")