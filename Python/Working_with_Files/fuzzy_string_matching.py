from thefuzz import process, fuzz

# Canonical list of company names
canonical_names = ['Apple Inc.', 'Google LLC', 'Microsoft Corporation']

# Raw data with variations
raw_data = ['Apple', 'Google', 'Microsoft Corp.', 'Aple Inc.']

print("Canonical list of company names: \n", canonical_names)
print("\nRaw data with variations: \n", raw_data)

cleaned_data = {}
for name in raw_data:
    # Find the best match from the canonical list with a cutoff of 85
    match = process.extractOne(name, canonical_names, score_cutoff=85)
    if match:
        # Map the raw name to its canonical version
        cleaned_data[name] = match[0]
    else:
        cleaned_data[name] = 'No match found'

print("\nAfter of Fuzzy String Matching:\n",cleaned_data)