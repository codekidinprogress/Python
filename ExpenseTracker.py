FILE_NAME = "expenses.txt"

while True:
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter category: ")
        amount = input("Enter amount: ")
        note = input("Enter note: ")

        with open(FILE_NAME, "a") as file:
            file.write(f"{date} | {category} | {amount} | {note}\n")

        print("Expense added successfully!")

    elif choice == "2":
        try:
            with open(FILE_NAME, "r") as file:
                print("\n--- Your Expenses ---")
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No expenses found.")

    elif choice == "3":
        total = 0
        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    parts = line.split("|")
                    total += float(parts[2])
            print("Total Expense: ₹", total)
        except FileNotFoundError:
            print("No expenses found.")
        except ValueError:
            print("Error reading expense amounts.")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
