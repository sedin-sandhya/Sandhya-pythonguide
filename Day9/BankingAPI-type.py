# Rewrites BankAccount using the typing module: Optional[str], List[Transaction], Dict[str, 
# BankAccount], and Callable[[Transaction], None]. @dataclass auto-generates __init__ and __repr__ 
# for Transaction. 
# mypy catches type errors statically before runtime. 
# Type annotations are now required in all production Python at Google, Meta, and Stripe.
# Rewrite BankAccount from Day 6 with full type annotations. 
# Use @dataclass for Transaction. 
# Run mypy until zero errors.


from typing import Optional, List
from dataclasses import dataclass

@dataclass
class Transaction:

    type : str
    amount : float
    balance : float
    note : Optional[str] = None

class BankAccount:

    def __init__(self, holder : str, acc_num : str, balance : float = 0.0) -> None:

        self.holder : str = holder

        self.acc_num : str = acc_num

        self.balance : float = balance

        self.transactions: List[Transaction] = []

    def deposit(self, amount : float) -> None:

        self.balance += amount

        transaction = Transaction(
            type = "CR",
            amount = amount,
            balance = self.balance,
            note = "Deposit"
        )

        self.transactions.append(transaction)

    def withdraw(self, amount : float) -> bool:

        if amount > self.balance:
            return False
        
        self.balance -= amount

        transaction = Transaction(
            type = "DR",
            amount = amount,
            balance = self.balance,
            note = "Withdraw"
        )

        self.transactions.append(transaction)

        return True
    
    def mini_statement(self) -> List[str]:

        statement : List[str] = []

        for t in self.transactions:

            line = (
                f"{t.type} "
                f"{t.amount} "
                f"Balance:{t.balance}"
            )

            statement.append(line)

        return statement

def main() -> None:

    account = BankAccount(
        holder = "Sandhya",
        acc_num = "10001",
        balance = 5000
    )
    account.deposit(2000)

    account.withdraw(1000)

    print(account.mini_statement())

if __name__ == "__main__":
    main()