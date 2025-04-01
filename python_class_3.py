class Account:
    def __init__(self, acc_number, name, balance):
        self.acc_number = acc_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit was successful. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def details(self):
        print(f"Account number: {self.acc_number}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")
        print("_______________")


acc1 = Account(acc_number="001", name="Boss Potatoes", balance=200000)
acc2 = Account(acc_number="002", name="Chupapi Munyanyo", balance=70000)

acc1.deposit(1000)
acc1.withdraw(200)
acc1.details()


#care [make, model, date_of_make, drive_side]
# get_age
# allowed_in_kenya
# print_details