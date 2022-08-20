#Exercício 008 #
#
# Escreva um programa que leia um valor em metros e exiba o valor convertido em: centímetros e melímetros


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 008 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Insserindo o valor em metros
m = int(input('Digite um valor em metros: '))

# Mostrando o valor em metros convertido em cm e mm
print('Para {}[m], temos: \n{}[dm] \n{}[cm] \n{}[mm] \n{}[km] \n{}[hm] \n{}[dam]'
      .format(m, (m*10), (m*100), (m*1000), (m/10), (m/100), (m/1000)))
