numeric_values = [
    99, 350, 499, 500, 501, 750, 999, 1000, 1001, 1499, 1500, 1501, 1750,
    1999, 2000, 2001, 2500, 2501, 3000, 3001, 4500, 4501, 5000, 5001, 10000, 10001, 15000, 15001
]

prefixes = ["k", "Sk", "ck"]
suffixes = [""]

def generate_tax_codes(numeric_values, prefixes, suffixes):
    tax_codes = []
    for value in numeric_values:
        for prefix in prefixes:
            for suffix in suffixes:
                tax_codes.append(f"{prefix}{value}{suffix}")
    return tax_codes

generated_tax_codes = generate_tax_codes(numeric_values, prefixes, suffixes)

for code in generated_tax_codes:
    print(code)

