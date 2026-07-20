def show_balance(balance): 
    print(f"Your balance is : {balance}")
    
def deposit(): 
    amount = float(input("enter the amount you want to deposit:"))
    if amount <= 0:
        print("invalid input ")
        return 0
    else:
        return amount
    
def withdraw(balance): 
    amount = float(input("Enter the amount you want to withdraw:"))
    if amount <= 0:
        print("should be more than 0")
        return 0
    elif amount > balance:
        print("should be less than your balance")
        return 0
    else: 
        return amount

def main(): 
    balance = 0
    is_running = True
    
    while(is_running): 
        print("Welcome to Our bank ")
        print("What would you want to do :")
        print("1. Check balance ")
        print("2. deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Type 1-4 to use the service ")
        
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("invalid input try again")

    print("Thanks for using our service ")
            
if __name__ == '__main__':
    main()