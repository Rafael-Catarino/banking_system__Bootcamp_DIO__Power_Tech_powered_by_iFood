import os


def header_deposit():
    print("-" * 30)
    print("Depositar".center(30))
    print("-" * 30)


def deposit():
    header_deposit()
    value_deposit = float(input("Quanto você quer depositar: "))
    if value_deposit <= 0:
        print("""Depósito invalido.
Você não pode depositar um valor negativo ou um valor igual a 0.""")
        os.system("pause")
        return 0
    else:
        print(f"Seu depósito foi realizado com sucesso.")
        os.system("pause")
        return value_deposit
