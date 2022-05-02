while True:
    # print("select a Day: ")
    # print("1. SUNDAY")
    # print("2. MONDAY")
    # print("3. TUESDAY")
    # print("4. WEDNESDAY")
    # print("5. THURSDAY")
    # print("6. FRIDAY")
    # print("7. SATURDAY")

    print("Enter q or Q to Exit")

    Day = input("Choose a number: ")

    if Day == "q" or Day == "Q":
        break
    if Day == "1":
        print("The Selected day: " + "SUNDAY")
    elif Day == "2":
        print("The Selected day: " + "MONDAY")
    elif Day == "3":
        print("The Selected day: " + "TUESDAY")
    elif Day == "4":
        print("The Selected day: " + "WEDNESDAY")
    elif Day == "5":
        print("The Selected day: " + "THURSDAY")
    elif Day == "6":
        print("The Selected day: " + "FRIDAY")
    elif Day == "7":
        print("The Selected day: " + "SATURDAY")
    else:
        print('****** "You are Stupid" ******')


