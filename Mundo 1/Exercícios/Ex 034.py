print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 034 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

sal = float(input('Digite o salário, R$'))

if sal > 1250:
    print('\nVocê recebeu um aumento de 10%, seu novo salário é de R${}'.format((sal*0.1)+sal))
else:
    print('\nVocê recebeu um aumento de 15%, seu novo salário é de R${}'.format((sal*0.15)+sal))
