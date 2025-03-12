while True:
    print("\nChoose an example to see:")
    print("1. Counting up to a certain number")
    print("2. User input validation")
    print("3. Printing a pattern")
    print("4. Exiting the program")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("\nExample 1: Counting up to a certain number")
        num = 1
        while num <= 5:
            print(num)
            num += 1
    elif choice == '2':
        print("\nExample 2: User input validation")
        password = "secret"
        input_password = ""
        while input_password != password:
            input_password = input("Enter the password: ")
            if input_password != password:
                print("Incorrect password. Try again.")
        print("Access granted!")
    elif choice == '3':
        print("\nExample 3: Printing a pattern")
        row = 1
        while row <= 5:
            print("*" * row)
            row += 1
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

