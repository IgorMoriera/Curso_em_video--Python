# Exercício 096 #
#
# Faça um programa que tenha uma função chamada área() que recebe as dimensoes de um terreno retangular
#  (largura e comprimento) e mostra a área do terreno.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 096 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

def area():
    print('==' * 30)
    print('   Calculando a área de seu terreno   ')
    print('==' * 30)

    # Input das variáveis
    a = float(input('LARGURA (m): '))
    b = float(input('COMPRIMENTO (m): '))

    # Processamento das variáveis
    print(f'A área do seu terreno {a} x {b} é de {(a * b)}m^2.')
    print('--' * 30)

# Programa principal
area()
