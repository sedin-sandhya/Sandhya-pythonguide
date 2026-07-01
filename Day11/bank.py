"""Bank account module."""

import logging


class BankAccount:
    """Represents a bank account."""

    def __init__(
        self,
        account_number: str,
        balance: float,
    ) -> None:
        """Create bank account.

        Args:
            account_number: Account id.
            balance: Initial balance.

        """
        self.account_number = account_number
        self.balance = balance

    def deposit(
        self,
        amount: float,
    ) -> None:
        """Add money.

        Args:
            amount: Amount deposited.

        """
        self.balance = self.balance + amount


def main() -> None:
    """Run application."""
    logger = logging.getLogger(__name__)

    logging.basicConfig(
        level=logging.INFO,
    )

    account = BankAccount(
        "123",
        5000,
    )

    account.deposit(
        1000,
    )

    logger.info(
        account.balance,
    )


if __name__ == "__main__":
    main()
