# Exercício 031 #
#
# Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem,
# cobrando R$0,50 por km para viagens de até 200km a RS$0,45 para viagens mais longas.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 031 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

dist = float(input('Digite a dsitância da sua viagem [km]: '))

if dist <= 200:
    print('\nPara {}Km, o preço da sua viagem é de R${}.'.format(dist, dist*0.5))
else:
    print('\nPara {}Km, o preço da sua viagem é de R${}.'.format(dist, dist * 0.45))
