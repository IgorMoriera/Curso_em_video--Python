print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 044 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

print('\n{:=^40}'.format(' Lojas Moreira '))

valor = float(input('Entre com o valor do produto: R$'))

print('''Nossas condições de pagamento são:
  [ 1 ] á vista
  [ 2 ] á vista no cartão/cheque
  [ 3 ] 2x no cartão
  [ 4 ] 3x ou mais no cartão''')

condicao = int(input('Qual o modo de pagamento? '))

a = 1
b = 2
c = 3
d = 4

if condicao == a:
        total = valor - (valor*0.1)
        print('\nPagando à vista você tem \033[1;31m10% de desconto\033[m. '
              '\nO valor final da compra é de \033[1;32mR${}\033[m.'.format(total))

elif condicao == b:
    total = valor - (valor*0.05)
    print('\nPagando à vista no cartão, você \033[1;31m5% de desconto\033[m. '
          '\nO valor final da compra é de \033[1;32mR${}\033[m.'.format(total))

elif condicao == c:
    total = valor
    parcela = total / 2
    print('\nPagando em até 2x no cartão, \033[1;31mnão há descontos\033[m. '
          '\nO valor final da compra é de \033[1;32mR${}\033[m e '
          'você irá pagar 2x de \033[1;32mR${}\033[m. SEM JUROS!'.format(total, parcela))

elif condicao == d:
    total = valor + (valor*0.2)
    totalpar = int(input('\nQuantas parcela? '))
    parcela = total / totalpar
    print('Sua compra será parcelada em {}x de R${:.2f} no cartão. Com juros de \033[1;31m 20%\033[m. '
          '\nO valor final da compra é de \033[1;32mR${:.2f}\033[m.'
          .format(totalpar, parcela, total))

else:
    total = 0
    print('\n\033[1;31mOPCÇÃO INVÁLIDA de pagamento.\n\033[mTente novamente.')