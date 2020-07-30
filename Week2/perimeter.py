
w1 = float(input("Enter width: " ))
h1 = float(input("Enter height: " ))
w2 = float(input("Enter width: " ))
h2 = float(input("Enter height: " ))
price_per_metre = float(input("Enter price per metre: "))

total_fence = w1 + h1 + w2 + h2

total_cost = total_fence * price_per_metre

print("Total fence required = ", total_fence)
print("Total price = ", total_cost)