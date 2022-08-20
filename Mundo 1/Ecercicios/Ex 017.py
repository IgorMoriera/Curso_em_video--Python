print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 017 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)
import math

CO = float(input('Digite o valor do cateto oposto: '))
CA = float(input('Digite o valor do cateto adjacente: '))

H = math.hypot(CO, CA)

print('Dados os valores de C.O = {:.2f} e C.A = {:.2f}, temos que a hipotenusa vale H = {:.2f}'.format(CO, CA, H))