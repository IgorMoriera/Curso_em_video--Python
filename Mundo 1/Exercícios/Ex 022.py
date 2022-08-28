# Exercício 022 #
#
# Crie um programa que leia o nome completo de uma pessoa e mostre:
#  > O nome com todas as letras maiúsculas e minúsculas;
#  > Quantas letras ao todo (sem considerar espaços);
#  > Quantas letras tem o primeiro nome.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 022 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Entrando com o nome do usuário
nome = str(input('Digite seu nome completo: ')).strip()

# Salvando o nome em uma lista
list = nome.split()

# Mostrando resultados na tela
print('\n>> Nome em maiúsculo: ', nome.upper())                 # Nome em maiúsculo
print('>> Nome em minúsculo: ', nome.lower())                   # Nome em minúsculo
print('>> Quantidade de letras:', len(nome)-nome.count(' '))    # Qnt. de letras [sem espaços]
print('>> Quantidade de letras do 1ª nome:', len(list[0]))      # Qnt. de letras no 1º nome
