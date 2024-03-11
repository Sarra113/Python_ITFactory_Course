from BankAccount import BankAccount
from Bank import Bank


contul_meu = BankAccount(2345, 'Ioana')
contul_meu2 = BankAccount(1333, 'Cristi')
print(contul_meu.add_money(100))
print(contul_meu.add_money(500))
print(contul_meu2.add_money(400))
print(contul_meu.withdraw(200))
print(contul_meu2.withdraw(1000))
contul_meu.available_funds()
contul_meu2.available_funds()


banca1 = Bank('BT')
banca1.add_account(contul_meu)
banca1.show_accounts()
banca1.add_account(contul_meu2)
banca1.show_accounts()
print(banca1.accounts)

print(banca1.money_transfer(2345, 1333, 50))




