print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 022 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

nome = str(input('Digite seu nome completo: '))
list = nome.split()

print('Nome em maiusculo: ', nome.upper())
print('Nome em minusculo: ', nome.lower())
print('Quantidade de letras:', len(nome.strip()))
print('Quantidade de letras do 1ª nome:', len(list[0]))
