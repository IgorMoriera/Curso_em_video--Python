# Exercício 002 #
#
# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 002 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Perguntando ao usuário o seu nome
nome = input('Digite seu nome: ')

# Escrevendo uma mensagem para o usuário
print('É um prazer de conhecer, {}!'.format(nome))