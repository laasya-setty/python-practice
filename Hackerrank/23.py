meal_cost = float(input().strip())

tip_percent = int(input().strip())
tax_percent = int(input().strip())
tip=(meal_cost/100)*tip_percent
tax=(tax_percent/100)*meal_cost
total=meal_cost+tip+tax
print(tip)
print(tax)
print(total)