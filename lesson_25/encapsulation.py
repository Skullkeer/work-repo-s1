class BankAccount:
    # initializer method
    # called automatically
    def __init__(self, name, value, acctype):
        self.__value = value # Needs to be private
        self.name = name # Okay to keep public
        self.__acctype = acctype

    def display(self):
        print(f"Account name:   {self.name}")
        print(f"Balance:        ${self.__value}")
        print(f"Account type:   {self.__acctype}")

    def withdraw(self, change):
        if change < self.__value:
            self.__value -= change
        else:
            raise Exception("Not enough funds!")

################################################
# pretend this is a seperate file

acct = BankAccount("Jadey", 10000000, "Checking")
acct.display()
acct.withdraw(100)
acct.display()
