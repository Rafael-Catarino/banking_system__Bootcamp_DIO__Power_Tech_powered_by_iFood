from deposit import deposit
from withdraw_money import withdraw_money
from extract import extract
import os


def header():
    print("-"*30)
    print("Banco".center(30))
    print("-" * 30)


def start_program():
    bank_account = 0
    withdrawal_number = 0
    # Definindo uma constant.
    WITHDRAWAL_LIMIT = 3
    arr_extract = []
    while True:
        os.system("cls")
        header()
        try:
            num = int(input("Digite:\n [1] Depositar\n [2] Sacar\n [3] Extrato\n [0] Sair\nInformar sua opção: "))
            if num == 0:
                break
            elif num == 1:
                os.system("cls")
                value = deposit()
                bank_account += value
                arr_extract.append(["Deposito", value])
            elif num == 2:
                os.system("cls")
                if withdrawal_number >= WITHDRAWAL_LIMIT:
                    print("Seu limite de saque diário foi atingido.")
                    os.system("pause")
                else:
                    value = withdraw_money(bank_account)
                    if not value <= 0:
                        bank_account -= value
                        arr_extract.append(["Saque", value])
                    else:
                        print("Você não pode sacar valor igual a 0 ou menor que zero.")
                        os.system("pause")
                        withdrawal_number -= 1
                withdrawal_number += 1
            elif num == 3:
                os.system("cls")
                extract(bank_account, arr_extract)
            else:
                os.system("cls")
                print("Você informou um número invalido.")
                print("Favor informar outra opção.")
                os.system("pause")
        except ValueError:
            print("Valor invalido:")
            os.system("pause")


start_program()
