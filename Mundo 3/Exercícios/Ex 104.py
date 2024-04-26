# Exercício 104 #
#
# Crie um programa que tenha a função leiaInt() que vai funcionar de forma semelhante á função input() do Python,
#  so que fazendo a validação para aceitar apenas um valor numérico.
#
# Exemplo: n = leiaInt(‘Digite um n: ‘)

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 104 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)


def leiaInt(msg):
    teste_logico = False
    valor = 0

    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            teste_logico = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')

        if teste_logico:
            break
    return valor


num_escolhido = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num_escolhido}')
