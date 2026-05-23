import re

# --- Data ---
transactions = [
    {'transaction_id': 1, 'description': 'Sale of PROD-481a for $299'},
    {'transaction_id': 2, 'description': 'Item PROD-92841 sold'},
    {'transaction_id': 3, 'description': 'Returned Item (PROD-552)'},
    {'transaction_id': 4, 'description': 'Misc sale, no product code'}
]

# --- Data Preview 1: The Original Data ---
print("--- Original Sales Transactions (List of Dictionaries) ---")
# We loop through the list to print each record in its initial state.
for transaction in transactions:
    print(transaction)
print("-" * 55) # Separator for clarity
def extract_product_id(description):
    match = re.search(r'(PROD-[\w-]+)', description)

    # If a match is found, return the captured group. Otherwise, return None.
    if match:
        return match.group(1)
    return None

# --- Applying the Function with a Loop and Previews ---
print("\n--- Processing Each Transaction and Extracting IDs ---")
# We use a standard 'for' loop to iterate over our list of dictionaries.
for transaction in transactions:
    # Preview of the current record being processed
    print(f"\nProcessing transaction_id: {transaction['transaction_id']}")

    # Access the 'description' value.
    desc = transaction['description']
    print(f"  -> Description: '{desc}'")

    # Call our function to get the product_id.
    product_id = extract_product_id(desc)
    print(f"  -> Extracted ID: {product_id}")

    # Add the new key-value pair to the dictionary.
    transaction['product_id'] = product_id

    # Preview of the record after modification
    print(f"  -> Record after update: {transaction}")
print("-" * 55)

# --- Data Preview 2: The Final, Transformed Data ---
print("\n--- Final Transactions after Extracting Product IDs ---")
for transaction in transactions:
    print(transaction)