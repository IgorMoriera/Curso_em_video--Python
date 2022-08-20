print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 018 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

import math

ang = float(input('Digite o valor do angulo: '))

sen = math.sin(ang)
cos = math.cos(ang)
tan = math.tan(ang)

print('Para um angulo de {}º, temos: \nCos = {:.2f} \nSen = {:.2f} \nTan = {:.2f}'.format(ang, sen, cos, tan))
