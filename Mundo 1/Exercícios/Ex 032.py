print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 032 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

import datetime

ano = int(input('Digite um ano qualquer: '))

if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('\nO ano {} é um ano BISSEXTO.'.format(ano))
else:
    print('\nO ano {} não é um ano BISSEXTO.'.format(ano))
