# Exercício 063 #
#
# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
# Sequência de Fibonacci. Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8 ...

print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 063 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

print('=========================================')
print('         Sequência de Fibonacci        ')
print('=========================================')
n = int(input('Digite a quantidade de termos desejada: '))

cont = 3
f = 0
f1 = f2 = 1
print('-~' * 25)
print('A sequência de Fibonacci para os {} primeiros termos é: '.format(f))
print('{}  {} '.format(f1, f2), end=' ')

while cont <= n:
    f = f2 + f1
    # Meu penultimo termo (f1) será o meu último termo última interação (f2)
    f1 = f2
    # O termo (f) será meu último termo (f2)
    f2 = f
    cont += 1

    print('{} '.format(f), end=' ')

print('. . .')