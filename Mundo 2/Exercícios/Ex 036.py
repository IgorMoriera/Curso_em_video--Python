print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 036 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

from time import sleep

valor_casa = float(input('\nQual o valor da casa? R$'))
salario = float(input('Qual o seu salário ? R$'))
anos_parc = int(input('Em quantos anos você pretende pagar sua casa? '))

prestacao = valor_casa / (anos_parc*12)

print('\nAnalisando . . .\n')
sleep(1)

print('Você vai pagar R${:.2f} por mês durante {:.1f} anos. Sem juros!'.format(prestacao, anos_parc))

if prestacao >= (0.3*salario):
    print('Empréstimo \033[1;31mNEGADO!\033[m')
else:
    print('Empréstimo \033[1;32mAPROVADO!\033[m')