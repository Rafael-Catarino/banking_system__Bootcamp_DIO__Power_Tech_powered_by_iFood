import os


def header_withdraw_money():
    print("-" * 30)
    print("Sacar".center(30))
    print("-" * 30)


def withdraw_money(bank_account):
    header_withdraw_money()
    withdraw = float(input("Valor do saque: "))
    if withdraw > bank_account:
        print("Saldo insuficiente.")
        os.system("pause")
        return 0
    elif withdraw > 500:
        print("Seu limite maximo por saque é de R$ 500,00.")
        os.system("pause")
        return 0
    else:
        return withdraw
