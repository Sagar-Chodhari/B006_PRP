class BankAccount:
    """Represents an account held at a simple bank."""
    bank_name = "National Bank"
    total_accounts = 0
    total_bank_balance = 0

    def __init__(self, account_holder, initial_deposit):
        """Open a new account for the holder with a starting deposit."""
        self.account_holder = account_holder
        self.balance = initial_deposit

        BankAccount.total_accounts += 1
        BankAccount.total_bank_balance += initial_deposit

    def __str__(self):
        return (
            f"{self.account_holder} holds ${self.balance:.2f} "
            f"in {self.bank_name}."
        )

    def deposit(self, amount):
        """Add funds to this account and update the bank total."""
        if amount > 0:
            self.balance += amount
            BankAccount.total_bank_balance += amount
            print(
                f"{self.account_holder} now has ${self.balance:.2f} "
                f"after depositing ${amount:.2f}."
            )
        else:
            print(f"{self.account_holder}, deposits must be positive.")

    def withdraw(self, amount):
        """Take money out of the account if funds allow."""
        if amount <= 0:
            print(f"{self.account_holder}, enter a positive withdrawal amount.")
        elif amount > self.balance:
            print(
                f"{self.account_holder}, you can only withdraw up to ${self.balance:.2f}."
            )
        else:
            self.balance -= amount
            BankAccount.total_bank_balance -= amount
            print(
                f"{self.account_holder} withdrew ${amount:.2f}. "
                f"Remaining balance: ${self.balance:.2f}."
            )

    def display_account_info(self):
        print(f"\n{self.account_holder}'s Account")
        print("------------------------")
        print(f"Balance available: ${self.balance:.2f}")
        print("Status:", self.__str__())

    @classmethod
    def display_bank_summary(cls):
        print("\nBank Summary")
        print("------------")
        print(f"Bank Name: {cls.bank_name}")
        print(f"Total Accounts: {cls.total_accounts}")
        print(f"Total Bank Balance: ${cls.total_bank_balance:.2f}")



def prompt_account(accounts):
    while True:
        print("\nPick an account:")
        for idx, account in enumerate(accounts, 1):
            print(f"  {idx}. {account.account_holder}")
        choice = input("Choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(accounts):
            return accounts[int(choice) - 1]
        print("Try again with a valid number.")


def main():
    accounts = [BankAccount("Alice", 1000), BankAccount("Bob", 500)]
    actions = {
        "1": "deposit",
        "2": "withdraw",
        "3": "show account",
        "4": "show bank summary",
        "5": "exit",
    }
    while True:
        print("\nWhat would you like to do?")
        for key, label in actions.items():
            print(f"  {key}. {label}")
        choice = input("> ")
        if choice == "5":
            print("Bye!")
            break
        if choice == "4":
            BankAccount.display_bank_summary()
            continue
        if choice in {"1", "2", "3"}:
            account = prompt_account(accounts)
            if choice == "1":
                try:
                    amount = float(input("Deposit amount: "))
                except ValueError:
                    print("Numbers only please.")
                    continue
                account.deposit(amount)
            elif choice == "2":
                try:
                    amount = float(input("Withdrawal amount: "))
                except ValueError:
                    print("Numbers only please.")
                    continue
                account.withdraw(amount)
            else:
                account.display_account_info()
        else:
            print("Pick a valid option from the list.")


if __name__ == "__main__":
    main()