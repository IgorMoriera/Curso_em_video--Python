print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 064 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

n = soma = cont = 0

while n != 999:
    n = int(input('Digite um número inteiro: '))

    cont += 1
    soma += n

soma = soma - 999
cont = cont -1

print('Você saiu.')
print('Você digitou {} números e a soma entre eles deu: {}.'.format(cont -1, soma - 999))
