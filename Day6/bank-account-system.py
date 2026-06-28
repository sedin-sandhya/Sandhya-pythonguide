# BankAccount class with __init__, deposit(), withdraw(), get_balance(), mini_statement(), and __str__.
# Stores the last 5 transactions as a list of dicts recording type 
# (CR/DR), amount, and running balance.
#  __str__ returns a one-line summary. 
# This exact pattern is used in every fintech backend.
# BankAccount class with deposit, withdraw, balance, and mini statement of last 5 transactions

class BankAccount:

    def __init__(self, holder_name, balance = 0):

        self.holder_name = holder_name
        self.balance = balance

        self.transactions = []

    def deposit(self, amount):

        self.balance += amount
        self.add_transaction("CR", amount)

        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):

        if self.balance < amount:
            print("Insufficient balance")
            return
        
        self.balance -= amount
        self.add_transaction("DR", amount)

        print(f"Withdrawn ₹{amount}")

    def add_transaction(self, type, amount):
        transaction = {
            "type": type,
            "amount": amount,
            "balance": self.balance
        }

        self.transactions.append(transaction)

        if(len(self.transactions) > 5):
            self.transactions.pop(0)

    def mini_statement(self):
        print("="*14)
        print("Mini Statement")
        print("="*14)

        for t in self.transactions:
            if t["type"] == "CR":
                print(
                    t["type"],
                    "+₹" + str(t["amount"]),
                    "Balance:", t["balance"]
                )
            else:
                print(
                    t["type"],
                    "-₹" + str(t["amount"]),
                    "Balance:", t["balance"]
                )
    
    def __str__(self):
        return (
            f"Account Holder: {self.holder_name}\n"
            f"Balance: {self.balance}" 
        )
    
def main():
    account = BankAccount("Sandhya", 5000)

    account.deposit(2000)
    account.withdraw(3000)
    account.deposit(500)

    print(account)

    account.mini_statement()

if __name__ == "__main__":
    main()