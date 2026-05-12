# Lists
monthly_sales     = [18500, 22400, 17300, 29800, 31000]
base_prices       = [999.4, 349.85, 89.00, 45.1, 129.9]
transaction_log   = [1042, 1087, 1042, 1101, 1087, 1205, 1042]
product_names     = ["Laptop", "Monitor", "Keyboard", "Mouse", "Headset"]
raw_emails        = ["alice@co.com", "bob@co.com", "alice@co.com", "carol@co.com", "bob@co.com"]
order_log         = ["Electronics", "Furniture", "Electronics", "Stationery", "Electronics", "Furniture"]
active_status     = [True, True, False, True, False]
pending_shipments = []                                                        # empty — useful as a collector

# Dictionaries
category_counts = {}                                                          # empty — useful as a collector
employee        = {"id": 1042, "name": "Sarah", "department": "Sales"}
product         = {"name": "Laptop", "price": 999.99, "stock": 42, "in_stock": True}
monthly_targets = {"North": 30000, "South": 25000, "East": 27000}
branch_scores   = {"Phoenix": 91, "Austin": 87, "Denver": 95, "Boston": 88}
prices          = {"Laptop": 999, "Monitor": 349, "Keyboard": 89}
employees = [                                                                 # list of dictionaries
    {"id": 1, "name": "Alice",   "dept": "Sales", "sales": 54000},
    {"id": 2, "name": "Bob",     "dept": "IT",    "sales": 0},
    {"id": 3, "name": "Charlie", "dept": "Sales", "sales": 48000},
]
raw_orders = [
    {"id": 1, "region": "North", "product": "Laptop",   "amount": 999},
    {"id": 2, "region": "South", "product": "Monitor",  "amount": 349},
    {"id": 3, "region": "North", "product": "Laptop",   "amount": 999},
    {"id": 4, "region": "East",  "product": "Keyboard", "amount": 89},
    {"id": 5, "region": "South", "product": "Laptop",   "amount": 999},
    {"id": 6, "region": "East",  "product": "Monitor",  "amount": 349},
    {"id": 7, "region": "North", "product": "Headset",  "amount": 129},
]

# Tuples
branch_location = (33.4484, -112.0740)                                       # (latitude, longitude) for Phoenix
shipment_status = ("Delivered", "Pending", "Delivered", "Failed", "Delivered")

# Sets
jan_buyers      = {"Alice", "Bob", "Charlie", "Diana"}
feb_buyers      = {"Bob", "Eve", "Alice", "Frank"}
active_branches = {"North", "South", "East"}
international   = {"Europe", "Asia", "LatAm"}

# [List] Indexing
product_names[0]    # Laptop
product_names[2]    # Keyboard
product_names[-1]   # Headset

# [List] Slicing: list[start:stop] — stop index is NOT included
top_sellers = product_names[0:3]    # ['Laptop', 'Monitor', 'Keyboard']
last_two    = product_names[3:]     # ['Mouse', 'Headset']
first_three = monthly_sales[:3]     # [18500, 22400, 17300]

# [List] Mutability — modify a value directly by targeting its index
monthly_sales[2] = 19800            # [18500, 22400, 19800, 29800, 31000]

# [List] copy() Trap — alias shares the same list object; .copy() creates an independent one
alias_products = product_names
alias_products.append("Joystick")
product_names                       # ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Headset', 'Joystick']

safe_copy = product_names.copy()
safe_copy.append("Microphone")
product_names                       # ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Headset', 'Joystick'] — untouched

# [List] Methods: append(), insert(), remove(), pop()
safe_copy.append("Webcam")
safe_copy.insert(1, "Laptop Stand")
safe_copy.remove("Laptop Stand")
last_removed = safe_copy.pop()      # "Webcam"
safe_copy                           # ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Headset', 'Joystick', 'Microphone']

# [List] Methods: sort(), reverse()
monthly_sales.sort()                # [18500, 19800, 22400, 29800, 31000]
monthly_sales.reverse()             # [31000, 29800, 22400, 19800, 18500]

# [List] Searching: count(), index()
active_count    = active_status.count(True)   # 3
first_false_pos = active_status.index(False)  # 2

# List comprehensions
taxed_prices   = [round(p * 1.12, 2) for p in base_prices]             # [1119.33, 391.83, 99.68, 50.51, 145.49]
premium_prices = [round(p * 1.12, 2) for p in base_prices if p > 200]  # [1119.33, 391.83]

# [DICTIONARIES] Access
product["name"]    # Laptop
product["price"]   # 999.99

# [DICTIONARIES] Update, add, delete
product["price"]    = 899.99   # overwrite existing value
product["warranty"] = "2yr"    # key didn't exist — Python creates it
del product["in_stock"]
product                        # {'name': 'Laptop', 'price': 899.99, 'stock': 42, 'warranty': '2yr'}

# [DICTIONARIES] Safe lookup — .get() returns a default value instead of raising a KeyError
email = employee.get("email", "No email found")    # No email found

# [DICTIONARIES] Looping with .items(), .keys(), .values()
region_lines = [f"Region: {r} | Target: ${t:,}" for r, t in monthly_targets.items()]
region_lines        # ['Region: North | Target: $30,000', 'Region: South | Target: $25,000', 'Region: East | Target: $27,000']

list(monthly_targets.keys())    # ['North', 'South', 'East']
list(monthly_targets.values())  # [30000, 25000, 27000]

# [DICTIONARIES] ounting pattern — check if key exists, increment or initialise
for category in order_log:
    if category in category_counts:
        category_counts[category] += 1
    else:
        category_counts[category] = 1
category_counts     # {'Electronics': 3, 'Furniture': 2, 'Stationery': 1}

# List of dictionaries — access a field with chained [] on list index then key
employees[0]["name"]    # Alice
employees[2]["sales"]   # 48000

total_sales = 0
for emp in employees:
    if emp["dept"] == "Sales":
        total_sales += emp["sales"]
total_sales             # 102000

# sorted() on a dictionary iterates keys alphabetically
sorted_scores = {b: branch_scores[b] for b in sorted(branch_scores)}
sorted_scores           # {'Austin': 87, 'Boston': 88, 'Denver': 95, 'Phoenix': 91}

# Dictionary comprehensions
discounted            = {item: round(price * 0.90, 2) for item, price in prices.items()}
high_value_discounted = {item: round(price * 0.90, 2) for item, price in prices.items() if price > 100}
discounted            # {'Laptop': 899.1, 'Monitor': 314.1, 'Keyboard': 80.1}
high_value_discounted # {'Laptop': 899.1, 'Monitor': 314.1}

# [Tuple] Indexing — same syntax as lists, but assignment raises TypeError
branch_location[0]    # 33.4484
# branch_location[0] = 34.0  — TypeError: tuple object does not support item assignment

# [Tuple] Methods: count(), index(), len()
delivered_count = shipment_status.count("Delivered")  # 3
first_pending   = shipment_status.index("Pending")    # 1
total_shipments = len(shipment_status)                # 5

# [Tuple] Single-item tuple — trailing comma is required; without it () is just grouping
not_a_tuple = ("Phoenix")   # <class 'str'>
is_a_tuple  = ("Phoenix",)  # <class 'tuple'>
type(not_a_tuple)           # <class 'str'>
type(is_a_tuple)            # <class 'tuple'>

# [Sets] Creating a set — duplicates are silently dropped on conversion
unique_customers = set(transaction_log)                       # {1042, 1205, 1101, 1087}
len(unique_customers)                                         # 4

# Set operations — comparing two groups instantly
returning     = jan_buyers.intersection(feb_buyers)           # {'Alice', 'Bob'}
all_customers = jan_buyers.union(feb_buyers)                  # {'Frank', 'Eve', 'Charlie', 'Diana', 'Bob', 'Alice'}
at_risk       = jan_buyers.difference(feb_buyers)             # {'Charlie', 'Diana'}

# [Sets] Management: add(), remove(), isdisjoint()
active_branches.add("West")
active_branches.add("North")                                  # silently ignored — already exists
active_branches.remove("South")
no_overlap      = active_branches.isdisjoint(international)   # True
active_branches                                               # {'East', 'North', 'West'}

# Type conversion — List → Set → Tuple → List (the deduplication pipeline)
unique_emails = set(raw_emails)                               # {'alice@co.com', 'bob@co.com', 'carol@co.com'}
locked_emails = tuple(unique_emails)                          # ('bob@co.com', 'alice@co.com', 'carol@co.com')
final_emails  = sorted(list(locked_emails))                   # ['alice@co.com', 'bob@co.com', 'carol@co.com']

# COMBINED WORKFLOW — raw_orders pipeline
regions_active = set(order["region"] for order in raw_orders) # {'North', 'East', 'South'}

revenue_by_region = {}
for order in raw_orders:
    r = order["region"]
    if r in revenue_by_region:
        revenue_by_region[r] += order["amount"]
    else:
        revenue_by_region[r] = order["amount"]
revenue_by_region                                             # {'North': 2127, 'South': 1348, 'East': 438}

high_value_orders = [o for o in raw_orders if o["amount"] > 500]  # 3 orders above $500

summary = (
    ("North", revenue_by_region["North"]),
    ("South", revenue_by_region["South"]),
    ("East",  revenue_by_region["East"]),
)

# DASHBOARD — SUMMARY OUTPUT

print(
    "\n====================== OUTPUT DASHBOARD ======================\n"

    f"  LIST\n"
    f"    Taxed Prices (12%)     : {taxed_prices}\n"
    f"    Premium Only (>$200)   : {premium_prices}\n"
    f"    Active Count           : {active_count}  |  First False At Index : {first_false_pos}\n"
    f"    Monthly Sales (sorted) : {monthly_sales}\n"

    f"\n  DICTIONARY\n"
    f"    Updated Product Record : {product}\n"
    f"    Email Lookup (.get)    : {email}\n"
    f"    Category Counts        : {category_counts}\n"
    f"    Total Sales Revenue    : ${total_sales:,}\n"
    f"    Discounted Prices      : {discounted}\n"
    f"    High-Value Discount    : {high_value_discounted}\n"
    f"    Sorted Branch Scores   : {sorted_scores}\n"

    f"\n  TUPLE\n"
    f"    Branch Location        : {branch_location}\n"
    f"    Delivered              : {delivered_count}  |  First Pending At : {first_pending}  |  Total : {total_shipments}\n"

    f"\n  SET\n"
    f"    Unique Customers       : {unique_customers}\n"
    f"    Returning Buyers       : {returning}\n"
    f"    At-Risk (Jan only)     : {at_risk}\n"
    f"    Cleaned Emails         : {final_emails}\n"

    f"\n  PIPELINE (raw_orders)\n"
    f"    Active Regions         : {regions_active}\n"
    f"    Revenue by Region      : {revenue_by_region}\n"
    f"    High-Value Orders      : {len(high_value_orders)} orders above $500\n"
    f"    Locked Summary (tuple) : {summary}\n"

    "=====================================================================\n"
)
