a = int(input("Enter the number: "))

if a > 50:
    if a > 60:
        if a > 70:
            if a > 80:
                if a > 90 and a == 100:
                    print("O GRADE")
                else:
                    print("A GRADE")
            else:
                print("B GRADE")
        else:
            print("C GRADE")
    else:
        print("D GRADE")
else:
    print("FAIL")
