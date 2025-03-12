# Initialize dictionary to store account details
accounts = {}

# Function to create a new account
def createAccount(accountNumber, initialBalance):
    accounts[accountNumber] = {'balance': initialBalance, 'transactions': []}
    return "Account”,accountNumber, “created with an initial balance of $”,initialBalance

# Function to deposit money into an account
def deposit(accountNumber, amount):
    if accountNumber in accounts:
        accounts[accountNumber]['balance'] += amount
        accounts[accountNumber]['transactions'].append(('deposit', amount))
        return accounts[accountNumber]['balance']
    else:
        return "Account does not exist."

# Function to withdraw money from an account
def withdraw(accountNumber, amount):
    if accountNumber in accounts:
        if accounts[accountNumber]['balance'] >= amount:
            accounts[accountNumber]['balance'] -= amount
            accounts[accountNumber]['transactions'].append(('withdrawal', amount))
            return accounts[accountNumber]['balance']
        else:
            return "Insufficient funds."
    else:
        return "Account does not exist."

# Function to check balance of an account
def checkBalance(accountNumber):
    if accountNumber in accounts:
        return accounts[accountNumber]['balance']
    else:
        return "Account does not exist."

# Function to view transaction history of an account
def viewTransactionHistory(accountNumber):
    if accountNumber in accounts:
        return accounts[accountNumber]['transactions']
    else:
        return "Account does not exist."

# Text-based user interface
while True:
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View Transaction History")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        accNumber = input("Enter account number: ")
        initialBalance = float(input("Enter initial balance: "))
        print(createAccount(accNumber, initialBalance))

    elif choice == '2':
        accNumber = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        newBalance = deposit(accNumber, amount)
        if isinstance(newBalance, float):
            print(amount, "deposited into account",accNumber," New balance: $",newBalance)
        else:
            print(newBalance)

    elif choice == '3':
        accNumber = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        newBalance = withdraw(accNumber, amount)
        if isinstance(newBalance, float):
            print(amount,"withdrawn from account",accNumber," New balance: $",newBalance)
        else:
            print(newBalance)

    elif choice == '4':
        accNumber = input("Enter account number: ")
        balance = checkBalance(accNumber)
        if isinstance(balance, float):
            print("Balance in account",accNumber,": $",balance)
        else:
            print(balance)

    elif choice == '5':
        accNumber = input("Enter account number: ")
        transactionHistory = viewTransactionHistory(accNumber)
        if isinstance(transactionHistory, list):
            print("Transaction history for account",accNumber,":")
            for transaction in transactionHistory:
                print(transaction)
        else:
            print(transactionHistory)

    elif choice == '6':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please choose again.")
