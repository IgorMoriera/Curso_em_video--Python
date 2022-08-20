print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 096 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

def area(a, b):
    print(f'A área do seu terreno {a} x {b} é de {(a * b)}m^2.')


print('     Controle de Terenos')
print('--' * 15)

area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
