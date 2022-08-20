print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 026 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

frase = str(input('Digite uma frase: ')).strip().upper()

print('A quantidade de letras "a", é: '.format(frase.count('A')))
print('Posição da 1ª letra "a" da frase é: {}'.format(frase.find('A')+1))
print('Posição da última letra "a" da frase: {}'.format(frase.rfind('A')+1))
