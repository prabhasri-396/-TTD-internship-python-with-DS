print("---WELCOME TO FYI---")
print("----------------------------------")
print("1. Shirt   - ₹1500")
print("2. Jeans   - ₹2000")
print("3. Jacket  - ₹3500")
print("4. Saree   - ₹4000")
print("----------------------------------")
choice = int(input("Select item (1-4): "))
qty = int(input("Enter quantity: "))
if choice == 1:
    item = "Shirt"
    price = 1500
elif choice == 2:
    item = "Jeans"
    price = 2000
elif choice == 3:
    item = "Jacket"
    price = 3500
elif choice == 4:
    item = "Saree"
    price = 4000
else:
    print("Invalid choice")
    exit()
tol = price * qty
if tol >= 5000:
    dist = tol * 0.20
elif tol >= 2000:
    dist = tol * 0.10
else:
    dist = 0
f_amount = tol - dist
print("\n BILL DETAILS")
print("----------------------------------")
print("Item       :", item)
print("Price      : ₹", price)
print("Quantity   :", qty)
print("Total      : ₹", tol)
print("Discount   : ₹", dist)
print("----------------------------------")
print("Payable    : ₹", f_amount)
print("Thank you for shopping.!")
