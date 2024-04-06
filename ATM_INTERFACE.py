def transfer( balance,transactions):
    if len(transactions) > 0:
        print("Transaction History: ")
        for transaction in transactions:
            print("- - - ", transaction)
        
        print("-----------------------------")
        print("Enter 1 for Balance Inquiry")
        print("Enter 2 for Money Withdrawal")
        print("Enter 3 for Money Deposit")
        print("Enter 4 for Money Transfer")
        print("Enter 5 to Quit.")

        option = int(input("Select an option (1/2/3/4/5): "))
        if option == 1:
            check_balance(balance,transactions)
        elif option == 2:
            withdraw(balance,transactions)
        elif option == 3:
            deposit(balance,transactions)
        elif option == 4:
            transfer(balance, transactions)
        elif option == 5:
            pass
        else:
            print("Invalid Option")
    else:
        print("No Transaction History")

def check_balance(balance,transactions):
    print("Your Current Balance is:", balance, "Rupees only")
    print("-----------------------------")
    print("Enter 1 for Balance Inquiry")
    print("Enter 2 for Money Withdrawal")
    print("Enter 3 for Money Deposit")
    print("Enter 4 for Money Transfer")
    print("Enter 5 to Quit.")
    
    option = int(input("Select an option (1/2/3/4/5): "))

    if option == 1:
        check_balance(balance,transactions)
    elif option == 2:
        withdraw(balance,transactions)
    elif option == 3:
        deposit(balance,transactions)
    elif option == 4:
        transfer(balance, transactions)
    elif option == 5:
        pass
    else:
        print("Invalid Option")

def deposit(balance, transactions):
    damount = int(input("Enter your Deposit amount: "))
    balance += damount
    transactions.append("Deposit Rs." + str(damount))
    print("Successfully Deposited")
    print("-----------------------------")
    print("Enter 1 for Balance Inquiry")
    print("Enter 2 for Money Withdrawal")
    print("Enter 3 for Money Deposit")
    print("Enter 4 for Money Transfer")
    print("Enter 5 to Quit.")
    
    option = int(input("Select an option (1/2/3/4/5): "))

    if option == 1:
        check_balance(balance, transactions)
    elif option == 2:
        withdraw(balance, transactions)
    elif option == 3:
        deposit(balance,transactions)
    elif option == 4:
        transfer(balance, transactions)
    elif option == 5:
        pass
    else:
        print("Invalid Option")

def withdraw(balance,transactions):
    amount = int(input("Enter the Withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        transactions.append("Withdraw Rs." + str(amount))
        print("Transaction Successful")
        print("-----------------------------")
        print("Enter 1 for Balance Inquiry")
        print("Enter 2 for Money Withdrawal")
        print("Enter 3 for Money Deposit")
        print("Enter 4 for Money Transfer")
        print("Enter 5 to Quit.")
        
        option = int(input("Select an option (1/2/3/4/5): "))

        if option == 1:
            check_balance(balance, transactions)
        elif option == 2:
            withdraw(balance, transactions)
        elif option == 3:
            deposit(balance, transactions)
        elif option == 4:
            transfer(balance, transactions)
        elif option == 5:
            pass
        else:
            print("Invalid Option")
    else:
        print("Insufficient Balance")

def auth():
    user_id = 1001
    pin = 1234

    id = int(input("Enter Your User ID: "))
    confirm_pin = int(input("Enter Your Pin: "))

    if pin == confirm_pin and user_id == id:
        main()
    else:
        print("Invalid User ID or Pin")
        auth()

def main():
    user_id = 1001
    pin = 1234
    balance = 1000000
    transactions = []

    print("Enter 1 for Balance Inquiry")
    print("Enter 2 for Money Withdrawal")
    print("Enter 3 for Money Deposit")
    print("Enter 4 for Money Transfer")
    print("Enter 5 to Quit.")
    
    option = int(input("Select an option (1/2/3/4/5): "))

    if option == 1:
        check_balance(balance, transactions)
    elif option == 2:
        withdraw(balance, transactions)
    elif option == 3:
        deposit(balance, transactions)
    elif option == 4:
        transfer(balance, transactions)
    elif option == 5:
        pass
    else:
        print("Invalid Option")


    print("Thank You, Visit Again")


if __name__ == "__main__":
    auth()
