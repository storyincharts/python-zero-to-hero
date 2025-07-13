## Basic currency converter
# Input: amount_in_usd=100 (Given exchange_rate_usd_Euro), output: Equivalent amount:85.0

#let's call usd = U, and Euro=E

U = int(input("USD value:"))
E = U * 0.85
print(f"Equivalent amount in EUR:{E}")