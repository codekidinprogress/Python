def login():
    print("Login feature coming soon...")
    pass

def register():
    print("Register feature coming soon...")
    pass

def dashboard():
    print("Welcome to Dashboard")
    print("1. View Profile")
    print("2. Settings")
    print("3. Logout")

def settings():
    # Settings feature will be added later
    pass

def main():
    while True:
        print("\n--- Application Menu ---")
        print("1. Login")
        print("2. Register")
        print("3. Dashboard")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            dashboard()
        elif choice == "4":
            print("Exiting application")
            break
        else:
            print("Invalid choice")

main()
