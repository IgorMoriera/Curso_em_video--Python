# Execício 015 #
#
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias
#  pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia
#  e R$0,15 por km rodado.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 015 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Inserindo a quantidade de dias alugados
qnt_dia = int(input('Digite a quantidade de dias: '))
# Inserindo a quantidade de km percorridos
qnt_km = float(input('Digite quantos Km rodados: '))

# Calculando o custo por dia do aluguel
custo_por_dia = qnt_dia * 60
# Calculando o custo por km percorrido
custo_km = qnt_km * 0.15
# Calculando o custo total a pagar pelo cliente
custo_total = custo_por_dia + custo_km

# Mostrando o valor ao usuário
print('O preço a pagar pelo aluguel é de R${:.2f}.'.format(custo_total))
