items = {
    "T-Shirt": 799,
    "Jeans": 1599,
    "Shoes": 2499,
    "Watch": 1999,
    "Headphones": 1299,
    "Backpack": 999,
    "Sunglasses": 899,
    "Wallet": 699,
    "Belt": 499,
    "Cap": 399
}
print("ORDER SUMMARY")
print("-" * 30)
total = 0
for item, price in items.items():
    print(item, ":", price)
    total += price
print("-" * 30)
print("Total Amount:", total)
state = input("Enter delivery state (South / East / North): ")
if state == "south":
    days = 1
elif state == "east":
    days = 3
elif state == "north":
    days = 5
else:
    days="currently not delivering"
print("\n Delivery Details")
print("Delivery State:", state.capitalize())
print("Estimated Delivery Time:", days, "day(s)")
