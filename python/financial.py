import os
import random
import datetime
import time
from functions_ import psswd_generator


def menu(bank):
    # done
    os.system("cls")

    while True:
        os.system("cls")
        ch = int(input("[1] nova conta | [2] adicionar dinheiro | [3] enviar dinheiro | [4] sair\n> "))

        if ch == 1:
            new_acc()
        elif ch == 2:
            add_money()
        elif ch == 3:
            send_money()
        elif ch == 4:
            return 0
        else:
            print("Valor errado!")
            time.sleep(1.5)
            continue


def acc_verify():
    # done
    while True:
        try:
            acc_num = input("Numero da conta: ")

            print("\n[+] Validando dados...")
            time.sleep(1.5)

            f = open(acc_num + ".txt", 'r')
            print("[+] Tudo certo!")
            time.sleep(0.7)
            break
        except:
            print("[!] A conta nao existe.\n")
            continue
    return acc_num


def bank_money():
    # done
    acc_num = acc_verify()
    f = open(acc_num + '.txt', 'r')
    s = []
    for i in f:
        s.append(i)

    z = int(s[0][6:])
    f.close()

    return z


def new_acc():
    # done
    num = random.randint(1000, 9999)
    name = input("Nome: ")
    bank = int(input("Valor atual: "))
    f = open(str(num) + ".txt", 'w')

    f.write("Banco: " + str(bank))
    f.write("Nome da conta: " + name + "\n")
    f.write("Numero da conta: " + str(num) + "\n")
    f.close()

    print("[+] Conta criada com sucesso !")
    time.sleep(1.5)


def send_money():
    acc_verify()
    qtd = int(input("Valor: "))


def add_money():
    date = datetime.datetime.now()
    acc_verify()

    qtd = int(input("Valor a adicionar: "))
    bank = bank_money()

    f = open(acc_num + '.txt', 'r')
    z = int(f.readline()[6:])
    f.close()

    f = open(acc_num + ".txt", 'a')
    f.write("\n===========================\n")
    f.write("= Modification @ {}/{}/{} =\n".format(date.day, date.month, date.year))
    f.write("===========================\n\n")
    f.write("Valor adicionado: {}\n".format(qtd))
    f.write("Valor atual: {}\n".format(bank))
    f.close()

    print("[+] Valor atual da conta:", bank)
    time.sleep(1.5)


bank = 700
if __name__ == '__main__':
    menu(bank)

