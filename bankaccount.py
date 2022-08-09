class BankAccount:
    def __init__(self, amount):
        self.balance = 0
        self.balance = self.balance + amount
        self.interest_rate = 0.01
        

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        # print(self.balance)
        return self

    def withdraw(self, amount):
        self.amount = amount
        if(self.balance <= amount):
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        else:
            self.balance = self.balance - amount
            # print (self.balance)
        return self
    def display_account_info(self):
        print(f"Balance: $ {self.balance}")
        return self

    def yield_interest(self):
        if(self.balance < 0):
            print("not interested")
        elif(self.balance > 0):
            # print(self.balance + (self.balance * self.interest_rate))
            return self
    # **Couldn't get this to print all instances of account info. Can be done within methods with a print...
    # @classmethod
    # def showmethemoney(cls):
    #     if(cls.deposit()):
    #         print(cls.balance)
    #     elif(account_1.withdraw()):
    #         print(account_1.balance)
    #     elif(account_1.yield_interest()):
    #         print(account_1.balance)
    #     elif(account_1.display_account_info()):
    #         print(account_1.balance)
    
account_1 = BankAccount(100)
account_2 = BankAccount(300)
account_1.deposit(490).deposit(50).deposit(200).yield_interest().display_account_info()
account_2.deposit(100).deposit(2000).withdraw(590).withdraw(95).withdraw(950).withdraw(850).yield_interest().display_account_info()

