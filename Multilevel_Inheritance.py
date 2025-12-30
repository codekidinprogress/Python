class Bank:
    def bank_info(self):
        print("Welcome to ABC Bank")

class Account(Bank):
    def create_account(self, name, acc_no):
        self.name = name
        self.acc_no = acc_no
        print(f"Account created for {self.name}")
        print(f"Account Number: {self.acc_no}")

class Transaction(Account):
    def deposit(self, amount):
        self.balance = amount
        print("Deposited Amount:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient Balance")
user = Transaction()
user.bank_info()
user.create_account("Amit", 123456)
user.deposit(5000)
user.withdraw(2000)
