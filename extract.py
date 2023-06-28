import locale
import os


def header_extract():
    print("-" * 30)
    print("Extrato".center(30))
    print("-" * 30)


def extract(bank_account, arr):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    header_extract()
    print("{:<10} - {:<10}".format("Transação", "Valor"))
    print("-"*30)
    for i in arr:
        print("{:<10} - {:<10}".format(i[0], locale.currency(i[1], grouping=True)))
    print("-" * 30)
    print("{:<10} - {:<10}".format("Saldo", locale.currency(bank_account, grouping=True)))
    os.system("pause")
