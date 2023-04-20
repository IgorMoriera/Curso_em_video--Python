# Exercício 041 #
#
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de uma atleta e mostre sua
# categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 ano: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima de> MASTER


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 041 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('\nSua categoria é \033[1;32mMIRIM\033[m, de acordo com sua idade de {} anos.'.format(idade))

elif 10 <= idade <= 14:
    print('\nSua categoria é \033[1;32mINFANTIL\033[m, de acordo com sua idade de {} anos.'.format(idade))

elif 15 <= idade <= 19:
    print('\nSua categoria é \033[1;32mJUNIOR\033[m, de acordo com sua idade de {} anos.'.format(idade))

elif idade == 20:
    print('\nSua categoria é \033[1;32mSÊNIOR\033[m, de acordo com sua idade de {} anos.'.format(idade))

elif idade > 20:
    print('\nSua categoria é \033[1;32mMASTER\033[m, de acordo com sua idade de {} anos.'.format(idade))
