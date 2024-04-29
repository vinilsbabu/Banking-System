from Banking_System import BankSystem


bank = BankSystem()

while True:
    print("Welcome to Banking System!!!")
    print("\n1. Create Account")
    print("2. Account Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone_number = input("Enter your phone number: ")
        address = input("Enter your address: ")
        initial_deposit = float(input("Enter initial deposit amount: "))
        username = input("Enter username: ")
        password = input("Enter password: ")
        bank.create_account(name, email, phone_number, address, initial_deposit, username, password)

    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        customer_id = bank.login(username, password)
        if customer_id:
            while True:
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. Display Account Information")
                print("4. Display Account Balance")
                print("5. Close Account")
                print("6. Logout")
                option = input("Enter your choice: ")

                if option == '1':
                    amount = float(input("Enter amount to deposit: "))
                    bank.deposit(customer_id, amount)

                elif option == '2':
                    amount = float(input("Enter amount to withdraw: "))
                    bank.withdraw(customer_id, amount)

                elif option == '3':
                    bank.display_account_info(customer_id)

                elif option == '4':
                    bank.display_balance(customer_id)

                elif option == '5':
                    bank.close_account(customer_id)
                    break

                elif option == '6':
                    break

                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Invalid username or password.")

    elif choice == '3':
        break

    else:
        print("Invalid choice. Please try again.")


