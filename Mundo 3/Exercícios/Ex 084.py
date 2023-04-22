# Exercício 084 #
#
# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, motre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.


print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 084 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

dados = list()
galera = list()

cont = maior = menor = 0

while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso[Kg]: ')))
    cont += 1

    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]

        if dados[1] < menor:
            menor = dados[1]

    galera.append(dados[:])
    dados.clear()

    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()

    while resposta not in 'SN':
        print('Resposta inválida. Tente novamente!')
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()
    print('--' * 20)

    if resposta == 'N':
        break

print(f'[ A ] - Foram registradas {cont} pessoa(s).')

print(f'[ B ] - O maior peso foi de {maior}Kg. Peso de ', end='')

for nome in galera:
    if nome[1] == maior:
        print(f'{nome[0]}...')

print(f'[ C ] - O menor peso foi de {menor}Kg. Peso de ', end='')
for nome in galera:
    if nome[1] == menor:
        print(f'{nome[0]}...', end='')
