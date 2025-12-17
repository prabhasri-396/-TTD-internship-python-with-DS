s = {
    "sri": "396",
    "madhu": "mad@123",
    "priya": "111",
    "tina": "tina@23",
    "subi": "000"
}
checks = 0
while checks < 3:
    uid = input("Enter login id: ")
    if uid in s:
        pwd = input("Enter password: ")
        if s[uid] == pwd:
            print("Login Successful!!!")
            break
        else:
            print("Wrong password")
    else:
        print("Invalid login id")
    checks += 1
if checks == 3:
    print("Too many wrong attempts")
    print("Please wait for 30 seconds...")
    print("You can try again now")
