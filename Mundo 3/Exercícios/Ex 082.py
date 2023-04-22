# Exercício 082 #
#
# Crie um programa que leia vários números e coloque-os em uma lista.
# Depois disso, crie duas lsitas extras que vão conter apenas os valores pares e os valores ímpares digitados
# respsctivamente. Ao final, mostre o conteúdo das 3 listas gereadas.


print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 082 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

lista = list()
par = list()
impar = list()

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()

    while resposta not in 'SN':
        print('Respsota incorreta. Tente novamente!')
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()

    if resposta == 'N':
        break

for val in lista:
    if val %2 == 0:
        par.append(val)
    else:
        impar.append(val)

lista.sort()
print('-=' *30)
print(f'Os valores digitados foram: {lista}')
print(f'Os valores PARES digitados foram: {par}')
print(f'Os valores ÍMPARES digitados foram: {impar}')
print('-=' *30)
