items = {
    "T-shirt": 500,
    "Jeans": 1200,
    "Shoes": 2500,
    "Jacket": 3000,
    "Sunglasses": 800,
    "Cap": 400,
    "Watch": 1500,
    "Bag": 1800,
    "Belt": 600,
    "Wallet": 700
}
print("Your Order List:")
total_amount = 0
for item, price in items.items():
    print(f"{item}: ₹{price}")
    total_amount += price
print("\nTotal Amount: ₹", total_amount)
city = input("\nEnter your city: ")
state = input("Enter your state (South/East/North): ").capitalize()
if state == "South":
    delivery_days = 1
elif state == "East":
    delivery_days = 3
else: 
    delivery_days = 5
print(f"\n Delivery Address: {city}, {state} State")
print(f"Estimated Delivery Time: {delivery_days} day(s)")
hours = float(input("\nEnter hours since order was placed: "))
if delivery_days == 1 and hours < 1:
    print("You can cancel your order completely (same city, within 1 hour).")
elif 1 <= hours <= 24:
    print("Partial refund available if you cancel now.")
else:
    print("Order cannot be cancelled now.")
