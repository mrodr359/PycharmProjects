
bubblegum = 202
toffee = 118
iceCream = 2250
milkChocolate = 1680
doughnut = 1075
pancake = 80


income = bubblegum + toffee + iceCream + milkChocolate + doughnut + pancake

print("Earned amount:")
print(f"Bubblegum: ${bubblegum}")
print(f"Toffee: ${toffee}")
print(f"Ice cream: ${iceCream}")
print(f"Milk chocolate: ${milkChocolate}")
print(f"Doughnut: ${doughnut}")
print(f"Pancake: ${pancake}")
print()
print(f"Income: {income}")



staff_expenses = input("Staff expenses:")
other_expenses = input("Other expenses:")

net_income = income - int(staff_expenses) - int(other_expenses)

print(f"Net income: ${net_income}")