import random

def psswd_generator(psswd_qtd, psswd_length):
    psswd_list = []
    chars= 'abcdefghijklmnopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ1234567890'

    for psswd in range(psswd_qtd):
        passwords = ''
        for n in range(psswd_length):
            passwords += random.choice(chars)
        psswd_list.append(passwords)

    for i in psswd_list:
        print(i)