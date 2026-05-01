units = int(input())
if units <= 199:
    bill = units * 1.20
elif units < 400:
    bill = units * 1.50
elif units < 600:
    bill = units * 1.80
else:
    bill = units * 2.00
if bill > 400:
    bill = bill + (0.15 * bill)
else:
    bill = bill + 100
print(f"{bill:.2f}")

