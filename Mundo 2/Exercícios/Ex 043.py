# Exercício 043 #
#
# desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o IMC e mostre seu status, de acordo com a
# tabela abaixo:
# - Abaixo de 18.5: ABAIXO DO PESO
# - Enntre 18.5 e 25: PESO IDEAL
# - 25 até 30: SOBREPESO
# - 30 até 40: OBESIDADE
# - Acima de 40: OBESIDADE MÓRBIDA


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 043 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

peso = float(input('\nDigite o seu peso [Kg]: '))
altura = float(input('Digite sua altura [m]: '))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print('Com um IMC de {:.2f}, você está abaixo do peso.'.format(IMC))

elif 18.5 < IMC < 25:
    print('Com um IMC de {:.2f}, você está no peso ideal.'.format(IMC))

elif 25 < IMC < 30:
    print('Com um IMC de {:.2f}, você está com sobrepeso.'.format(IMC))

elif 30 < IMC < 40:
    print('Com um IMC de {:.2f}, você está com obesidade.'.format(IMC))

elif IMC > 40:
    print('Com um IMC de {}, você está com obesidade mórbida.'.format(IMC))
