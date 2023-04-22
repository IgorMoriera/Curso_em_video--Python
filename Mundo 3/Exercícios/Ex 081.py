# Exercício 081 #
#
# Crie um programa que leia vários números e coloque-os em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrscente.
# C) Se o valor 5 foi digitado e está ou não na lista.


print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 081 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

n = list()

while True:
    num = int(input('Digite um valor: '))
    reposta = str(input('Você quer continuar? [S/N]: ')).upper().strip()
    n.append(num)


    while reposta not in 'SN':
        print('Resposta incorreta. Tente novamente!')
        reposta = str(input('Você quer continuar? [S/N]: ')).upper().strip()

    if reposta == 'N':
        break

print('-=' *30)

print(f'[ A ] - Você digitou {len(n)} números.')

n.sort(reverse=True)
print(f'[ B ] - A lista de froma decrescente fica: {n}.')

if 5 in n:
    print(f'[ C ] - O valor 5 foi digitado e está na posição: ', end='')
else:
    print(f'[ C ] - O valor 5 não foi digitado na lista!')

for pos, val in enumerate(n):
    if val == 5 in n:
        print(f'{pos+1}...', end='')
