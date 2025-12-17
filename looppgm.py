s = {"sri": "396",
    "madhu": "mad@123",
    "priya": "111",
    "tina": "tina@23",
    "subi": "000"}  
while True:
    print("\n===== MAIN MENU =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        uid = input("Enter new username: ")

        if uid in s:
            print("❌ Username already exists!")
        else:
            pwd = input("Enter new password: ")
            s[uid] = pwd
            print("✅ Registration successful!")

    elif choice == "2":
        if not s:
            print("⚠ No users registered yet!")
            continue

        print("\n🔐 Login (3 attempts only)")
        for check in range(1, 4):
            uid = input("Username: ")
            pwd = input("Password: ")

            if uid in s and s[uid] == pwd:
                print("🎉 Login successful! Welcome,", uid)
                break
            else:
                print("❌ Invalid credentials")

            if check == 3:
                print("🚫 Too many attempts! Login blocked.")

    elif choice == "3":
        print("👋 Program exited.thank you!")
        break

    else:
        print("⚠ Invalid choice! Try again.")
