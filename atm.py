import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


class BankAccount:
    def __init__(self, account_number, password, balance=0.0):
        self.__account_number = account_number
        self.__password = hash_password(password)
        self.__balance = balance

    def verify_password(self, password):
        return self.__password == hash_password(password)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print("Withdrawal successful.")

    def check_balance(self):
        print(f"Balance: {self.__balance}")


class ATM:
    def __init__(self):
        self.accounts = {}
        self.current_user = None

    def register(self):
        acc_num = input("Enter account number: ")
        password = input("Enter password: ")

        if acc_num in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[acc_num] = BankAccount(acc_num, password)
            print("Account created successfully.")

    def login(self):
        acc_num = input("Enter account number: ")
        password = input("Enter password: ")

        account = self.accounts.get(acc_num)

        if account and account.verify_password(password):
            self.current_user = account
            print("Login successful.")
        else:
            print("Invalid credentials.")

    def logout(self):
        self.current_user = None
        print("Logged out.")

    def menu(self):
        while True:
            print("\n1. Register\n2. Login\n3. Exit")
            choice = input("Choose: ")

            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
                if self.current_user:
                    self.user_menu()
            elif choice == "3":
                break
            else:
                print("Invalid option.")

    def user_menu(self):
        while self.current_user:
            print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Logout")
            choice = input("Choose: ")

            if choice == "1":
                amount = float(input("Enter amount: "))
                self.current_user.deposit(amount)

            elif choice == "2":
                amount = float(input("Enter amount: "))
                self.current_user.withdraw(amount)

            elif choice == "3":
                self.current_user.check_balance()

            elif choice == "4":
                self.logout()
            else:
                print("Invalid option.")


atm = ATM()
atm.menu()