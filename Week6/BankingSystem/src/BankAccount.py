

class BankAccount:
    def __init__(self, number: int, owner: str):
        self.number = number
        self.owner = owner
        self.__balance = 2999.99

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        raise PermissionError('Nu puteti modifica direct contul. Folositi operatiunile de depunere sau retragere')

    @balance.deleter
    def balance(self):
        raise PermissionError('Nu puteti sterge soldul')

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount
            return f'{amount} RON au fost depusi cu succes pe contul {self.number}. Soldul curent: {self.__balance} RON.'
        else:
            return 'Suma trebuie sa fie pozitiva'

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f'{amount} au fost retrasi cu succes de pe contul {self.number}. Sold curent: {self.__balance} RON.'
        elif amount <= 0:
            return 'Suma trebuie sa fie pozitiva'
        else:
            return 'Insufficient funds'

    def available_funds(self):
        print(f'The current balance of the account nr {self.number} is {self.__balance} RON.')
