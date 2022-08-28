# Exercício 026 #
#
# Faça um programa que leia uma frase pelo teclado e mostre:
#  > Quantas vezes aparece a letra "A"
#  > Em que posição ela aparece 'a' primira vez
#  > Em que posição ela aparece 'a' pela última vez


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 026 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Entrando com uma frase
frase = str(input('Digite uma frase: ')).strip().upper()

# Mostrando os resultados na tela
print('A quantidade de letras "a", é: '.format(frase.count('A')))               # Qnt de letras da frase digitada
print('Posição da 1ª letra "a" da frase é: {}'.format(frase.find('A')+1))       # Posição do primiero 'a' da frase
print('Posição da última letra "a" da frase: {}'.format(frase.rfind('A')+1))    # Posição do último 'a' da frase
