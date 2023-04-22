# Exercício 064 #
#
# Crie um proigrama que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos núemeros foram digitados e ual foi a soma
# entre eles (desconsiderando o flag).


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 064 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

n = soma = cont = 0

while n != 999:
    n = int(input('Digite um número inteiro: '))

    cont += 1
    soma += n

print('Você saiu.')
print('Você digitou {} números e a soma entre eles foi: {}.'.format(cont - 1, soma - 999))
