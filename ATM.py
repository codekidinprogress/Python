pin = 1234
balance = 5000

user_pin = int(input("Enter PIN: "))

if user_pin == pin:
    print("\nLogin Successful!\n")
    
    while True:
        print("----- ATM Menu -----")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("Current Balance:", balance)
        
        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawal Successful!")
                print("Remaining Balance:", balance)
            else:
                print("Insufficient Balance!")
        
        elif choice == 3:
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("Deposit Successful!")
            print("Updated Balance:", balance)
        
        elif choice == 4:
            print("Thank you for using ATM!")
            break
        
        else:
            print("Invalid choice! Try again.")
else:
    print("Incorrect PIN!")
