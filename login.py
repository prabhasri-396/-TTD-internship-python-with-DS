s = {
    "sri": "396",
    "madhu": "mad@123",
    "priya": "111",
    "tina": "tina@23",
    "subi": "000"
}

sid = input("Enter login id: ")

if sid in s:
    pwd = input("Enter password: ")
    if s[sid] == pwd:
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Login ID not found")
    choice = input("Do you want to create a new login? (yes/no): ")

    if choice.lower() == "yes":
        new_pwd = input("Create password: ")
        s[sid] = new_pwd
        print("New login created successfully!")
    else:
        print("Login cancelled")



