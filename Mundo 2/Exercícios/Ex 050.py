# Exercício 050 #
#
# Desenvolva um programa que leia 6 números e mostre a soma apenas daqueles que forem pares. Seo valor digitado for
# ìmpar deseconsidere-o.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 050 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

soma = 0

for n in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(n)))

    if num % 2 == 0:
        # poderia colocar: soma += num - para realizar o somatório abaixo .
        soma = soma + num
    
print('\nO somatório dos números pares acima deu: {}'.format(soma))
