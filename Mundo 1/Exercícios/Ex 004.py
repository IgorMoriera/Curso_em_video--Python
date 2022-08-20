# Exercício 004 #
#
# Faça um programa que leia algo pelo tecldo e mostre na tela o seu tipo primitivo
#  e todos as infomrações possíveis sobre ele.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 004 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Variável que lê qualquer coisa que o usuário digite na tela
algo = input('Digite algo: ')

# É alfa-numérico?
print('É alfa-numérico? ', algo.isalnum())

# É uma letra?
print('É uma letra? ', algo.isalpha())

# É numérico?
print('É numérico? ', algo.isnumeric())

# É um espaço?
print('É um espaço? ', algo.isspace())

# Está tudo em maiusculo?
print('Está tudo em maiusculo? ', algo.isupper())

# Está tudo em minusculo?
print('Está tudo em minusculo? ', algo.islower())
