import os
os.system("CLS")

# remover o while da internet , pois nao é mais necessário (l.14 resolve).
# corrigir erro quando usado valores negativos.
# criar handler quando as despesas sao maiores do que o ordenado 
# criar "tips" caso ^ seja verdade. 

def menu():
    nome = str(input('Olá, Digite seu nome: ')).title().strip()
    cores = {'roxo':'\033[1;35m', 'azul':'\033[;34m', 'red':'\033[1;31m','verde':'\033[;32m', 'fim':'\033[m', 'amarelo': '\033[;33m'}
    print('Hello {}{}{}!!! '.format(cores['roxo'], nome, cores['fim']))
    print('A partir de agora vou te auxiliar na sua gestão financeira.')
    print('Caso você não tenha alguma das faturas pedidas a seguir, coloque valor 0 (zero) nela.\n')
    money_manager(cores)


def money_manager(cores):
    ordenado = float(input('Digite o valor do seu Ordenado: '))

    #informaçôes sobre renda.
    renda = float(input('\nDigite o valor da Renda/Aluguel: '))

    # informações refente luz e gás 
    luz = float(input('Digite o valor da fatura de Luz: '))
    gas = float(input('Digite o valor da fatura de Gás: '))

    # informaçôes sobre água.
    agua = float(input('Digite o valor da fatura de Água: '))

    #informaçôes sobre internet
    while True:
        internet = str(input('\nVocê possui algum plano de internet em casa? (s/n): ')).strip().lower()

        if internet == 's':
            net = float(input('Digite o valor da fatura: '))
            break

        elif internet == 'n':
            net = 0
            break

        else:
            print("\n{}[-]{} Erro.".format(cores['red'], cores['fim']))
            continue

    calc(ordenado, renda, luz, agua, gas, net, cores)


def calc(ordenado, renda, luz, agua, gas, net, cores):
    total = 0

    porcentagem = 100 * renda / ordenado
    print('\nA porcentagem da despesa de aluguel é de: {}{:.2f}{} %'.format(cores['verde'], porcentagem, cores['fim']))
    total += renda

    porcentagem = 100 * luz / ordenado
    print('A porcentagem da despesa de luz é de: {}{:.2f}{} %'.format(cores['verde'], porcentagem, cores['fim']))
    total += luz

    porcentagem = 100 * agua / ordenado
    print('A porcentagem da despesa da água é de: {}{:.2f}{} %'.format(cores['verde'], porcentagem, cores['fim']))
    total += agua

    porcentagem = 100 * gas / ordenado
    print('A porcentagem da despesa de gás é de: {}{:.2f}{} %'.format(cores['verde'],porcentagem,cores['fim']))
    total += gas

    porcentagem = 100 * net / ordenado
    print('A porcentagem da dispesa de internet é de: {}{:.2f}{} %'.format(cores['verde'],porcentagem,cores['fim']))
    total += net 

    porcentagem = 100 * total / ordenado
    print("\nTotal das despesas: {} € | {:.2f} %".format(total, porcentagem))


# def more_bills <- funçao para caso o user qeira add mais despesas
menu()



"""
#adicionando novas dispesas 
açao = str(input('\nVai querer adicionar mais alguma dispesa? s ou n ?: ')).strip()
carteira = total
while açao == 's':
    variavel = str(input('\nDigite o nome da da dispesa para registrar: ')).title().strip()
    valor = float(input('\nQual o valor vai retirar para: {}{}{}?: '.format(cores['amarelo'],variavel,cores['fim'])))
    porcentagem = 100 * valor / ordenado
    carteira = carteira - valor  
    print('temos na carteira valor de total de: $ {}{:.2f}{}'.format(cores['azul'], carteira, cores['fim']))
    #print('Foi retirado: ${}{:.2f}{}, para {}{}{}, restando na carteira o valor de: ${}{:.2f}{}'.format(cores['azul'],valor,cores['fim'],cores['verde'],variavel,cores['fim'],cores['azul'],resto,cores['fim']))
    print('A porcentagem da dispesa, {}{}{}, é de: {}{:.2f}{} %'.format(cores['amarelo'], variavel, cores['fim'], cores['verde'], porcentagem, cores['fim']))
    açao = str(input('\nVai querer adicionar mais alguma dispesa? s ou n ?: ')).strip()
else:
    print('\nok, {}{}{}: temos na carteira valor total de: ${}{:.2f}{}'.format(cores['roxo'],nome,cores['fim'],cores['azul'],carteira,cores['fim']))


print('\33[7;30;41mPrograma ainda em desenvolvimento\... \33[m')
"""