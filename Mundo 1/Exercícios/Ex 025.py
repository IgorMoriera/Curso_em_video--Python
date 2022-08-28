# Exercício 025 #
#
# Crie um programa que leia um nome de uma pessoa e diga se ela tem 'SILVA' no nome


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 025 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Entrando com o nome
nome = str(input('Digite seu nome completo: ')).strip()

# Identificando se há ou não "SILVA" no nome digitado
print('SILVA' in nome.upper())