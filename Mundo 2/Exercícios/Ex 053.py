print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 053 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

frase = str(input('Digite uma frase: ')).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

# OBS: Outra forma de substituir o 'FOR' é fatiando a string com: inverso = junto[::-1]

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if junto == inverso:
    print('O inverso de {} é {}. Portanto a frase É UM PALÍNDROMO!'.format(junto, inverso))
else:
    print('O inverso de {} é {}. Portanto a frase  NÃO É UM PALÍNDROMO!'.format(junto, inverso))