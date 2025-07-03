try:
    a = int(input("Enter the num 1 : "))
    b = int(input("Enter the num 2 : "))

    print("For addition type (+)\nFor addition type (-)\nFor addition type (*)\nFor addition type (/)")

    o = input("Enter the operation which you want to perform : ")

    match o:
        case "+":
            print(f"The result is {a+b}")
        case "-":
            print(f"The result is {a-b}")
        case "*":
            print(f"The result is {a*b}")
        case "/":
            print(f"The result is {a/b}")
        case default:
            print("some error occured")


except Exception as e:
    print("Enter a valid input for a and b.")

        