# Exercício 057 #
#
# Faça um programa que leia o sexo de uma pessoa, mas só acieite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 057 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

masc = 'M'
femi = 'F'
sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual o seu sexo [M/F]: ')).upper().strip()[0]

    if sexo != 'F' or sexo != 'M':
        print('Dígito incorrreto.')

print('Sexo registrado com sucesso!')
