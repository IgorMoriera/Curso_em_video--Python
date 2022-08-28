# Exercício 024 #
#
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 024 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Entrando com o nome da cidade
nome_cidade = str(input('Digite o nome da sua cidade: ')).strip()

# Mostrando o resultado entre VERDADEIRO ou FALSO
print(nome_cidade[:5].upper() == 'SANTO')