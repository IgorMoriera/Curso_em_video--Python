# Exercício 033 #
#
# Faça um programa que leia três números e mostre qual deles é MAIOR e qual é o MENOR.


print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 033 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

a = int(input('Digite a 1º número: '))
b = int(input('Digite a 2º número: '))
c = int(input('Digite a 3º número: '))

menor = a

# Testando os menores valores
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Testando os maiores valores
if b > a and b > c:
    maior = b
if c < a and c < b:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O menor valor digitado foi {}'.format(maior))
