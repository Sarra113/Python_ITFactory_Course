from BankAccount import BankAccount


class Bank:

    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def add_account(self, account: BankAccount):
        self.accounts[account.number] = account

    def show_accounts(self):
        for number, account in self.accounts.items():
            print(f'Contul {number} este detinut de {account.owner} si are soldul de {account.balance}')

    def money_transfer(self, sender_nr, receiver_nr, amount):
        if sender_nr in self.accounts and receiver_nr in self.accounts:
            sender = self.accounts[sender_nr]
            receiver = self.accounts[receiver_nr]
            result1 = sender.withdraw(amount)
            result2 = receiver.add_money(amount)
            return f"Result after transactions: {result1} and {result2}"
        else:
            return "Conturi invalide"




