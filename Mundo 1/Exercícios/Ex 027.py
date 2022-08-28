# Exercício 027 #
#
# Faça um programa que leia o nome completo de uma pessoa,
#   mostrando em seguida o primeiro e o último nome separadamente.


print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 027 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

# Entrando com o nomo do usuário
nome = str(input('Digite seu nome completo: ')).strip() # Removendo os espaços
# Separando as palavras do nome [completo]  digitado através de uma lista
n = nome.split()

# Mostrando os resultados na tela
print('A lista gerada foi: {}'.format(n))      # Mostrando a lista para identificar a posição dos nomes
print('Seu nome começa com: {}'.format(n[0]))  # Pegando o primeiro nome da lista
print('E termina com: {}'.format(n[len(n)-1])) # Pegando o último nome da lista [qnt de palavras na lista - 1]
