import random
import datetime
import os
os.system("cls")
x = datetime.datetime.now()

def menu():
    print('Password Generator')
    print('==================')
    print('\n')

    while True:
        try:
            psswd_qtd = int(input("Number of passwords: "))
            psswd_length = int(input("Password length: "))
        except:
            print("Wrong value!\n")
            continue
        break

    psswd_generator(psswd_qtd, psswd_length)


def psswd_generator(psswd_qtd, psswd_length):
    psswd_list = []
    valid = 0

    print("\nType: (E)asy | (M)edium | (H)ard")

    while valid == 0:
        type = input("> ")
        if type.upper() == 'E':
            chars = 'abcdefghijklmnopqrstuvxywz'
            type = 'EASY'
            valid = 1
        elif type.upper() == 'M':
            chars= 'abcdefghijklmnopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ1234567890'
            type = 'MEDIUM'
            valid = 1
        elif type.upper() == 'H':
            chars = "abcdefghijklmnopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ!""'*-_.1234567890"
            type = 'HARD'
            valid = 1
        else:
            print("Error.")
            continue

    for psswd in range(psswd_qtd):
        passwords = ''
        for n in range(psswd_length):
            passwords += random.choice(chars)
        psswd_list.append(passwords)

    for i in psswd_list:
        print(i)
    
    while True:
        save = input("\nSave passwords (y/n): ")
        if save.lower() == 'y' or save.lower() == 'yes':
            psswd_save(psswd_list, type)
            break
    
        elif save.lower() == 'n' or save.lower() == 'no':
            break

        else:
            print("Error. Try again!")


def psswd_save(psswd_list, type):
    name = 'password_generator.txt'
    try:
        f = open(name, "a")
    except FileExistsError():
        f = open(name, "w")

    f.write("\n============\n")
    f.write("Added Password Type [{}] @ {}/{}/{}\n".format(type,x.day,x.month,x.year))
    f.write("============\n")

    for psswd in psswd_list:
        f.write(psswd + "\n")
    f.close()
    
    print("Saved!")
    print("File name: {}".format(name))


if __name__ == '__main__':
    menu()
