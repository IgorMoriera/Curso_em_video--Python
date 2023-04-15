# Exercício 029 #
#
# Escreva um programa que leia a velocidade de um carro.
# Se ela ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 029 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

v = float(input('Digite a velocidade do carro: '))
vp = 80

if v > vp:
    print('\nSua velocidade foi acima da permitida. '
          '\nO valor da multa é de R${:.2f}.'.format((v-80)*7))
else:
    print('\nVocê está dentro do limite permitido.')
