while True:
    print("select an operation to perform: ")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")

    print("Enter q or Q to Exit")

    operation = input("Enter Operation no: ")

    if operation == "q" or operation == "Q":
        break
    if operation == "1":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("The Sum is: " + str(int(num1) + int(num2)))
    elif operation == "2":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("The Difference is: " + str(int(num1) - int(num2)))
    elif operation == "3":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("The MULTIPLICATION is: " + str(int(num1) * int(num2)))
    elif operation == "4":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("The DIVISION is: " + str(int(num1) / int(num2)))
    else:
        print('****** "You are Stupid" ******')

