import os

clear = lambda: os.system('cls')
conta = 100.00
temp = 0
op = -1
def testesaque(temp, conta):
    if temp <= conta:
        return True
    else:
        return False


def saque(temp, conta):
    contasaque = 0
    contasaque = temp
    clear()
    print('Vc sacou {} reais:'.format(temp))
    return contasaque



def deposito(temp):
    clear()
    print('Voce depositou {}'.format(temp))
    return temp


def saldo(conta):
    clear()
    print('\nSeu saldo é R${}.\n'.format(conta))


while op != 0:

    print('-------------Banco K---------------\n'
          'Escolha sua opção:\n'
          '1 - Saldo:\n'
          '2 - Deposito:\n'
          '3 - Saque:\n'
          '0 - Sair:\n'
          '-------------------------------------')

    op = int(input("Digite a opção desejada:"))
    if op == 1:
        saldo(conta)
    elif op == 2:
        temp = float(input('Digite o valor a ser depositado:'))
        conta += deposito(temp)
    elif op == 3:
        temp = float(input('Digite o valor a ser sacado:'))
        if testesaque(temp, conta):
            conta -= saque(temp, conta)
        else:
            print('Você nao tem saldo')
