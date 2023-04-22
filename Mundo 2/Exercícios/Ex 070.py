# Exercícios 090 #
#
# Crie um programa que leia a nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto.
# B) Quantos produtos custam mais de R$100.
# C) QUal é o nome do produto mais barato.


print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 070 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

preco = menor = total = contpreco = cont = 0
produtobarato = ' '

print('--' * 15)
print('     LOJÃO DOS MOREIRAS')
print('--' * 15)

while True:
    nomeprod = str(input('Digite o nome do poduto: ')).strip()
    preco = float(input('Digite o preço: R$'))
    cont += 1

    # A
    total += preco

    # B
    if preco > 1000:
        contpreco += 1

    # C
    if cont == 1 or preco < menor:
        menor = preco
        produtobarato = nomeprod

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('\033[33mQuer continuar [S/N]?\033[m ')).upper().strip()[0]
    print('==' * 20)

    if opcao == 'N':
        break

print('-=' * 30)
print(f'''[ A ] - O total da compra foi de R${total:.2f}.
[ B ] - Ao todo foram {contpreco} produtos acima de R$1000,00.
[ C ] - O produto mais barato foi {produtobarato} que custa R${menor:.2f}.''')
print('-=' * 30)
