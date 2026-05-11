class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0
    def __init__(self, name: str, balance: float) -> None:
        self.name = name        # Instance: Each account has unique owner
        self.balance = balance  # Instance: Each account has unique balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance

    def print_balance(self):
        print(f"{self.name}'s balance: ${self.balance}")

    def print_total_accounts(self):
        print(f"Total Accounts: {BankAccount.total_accounts}")

    def print_total_balance(self):
        print(f"Total Balance: ${BankAccount.total_balance}")


# TODO: Create two accounts
# TODO: Print the information using the mentioned format
alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 2000) 

alice.print_balance()
bob.print_balance()
alice.print_total_accounts()
alice.print_total_balance()
