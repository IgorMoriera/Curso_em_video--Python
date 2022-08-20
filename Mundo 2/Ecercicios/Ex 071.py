print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 071 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

print('==' *15)
valor = int(input('Digite o valor do saque: R$'))
print('==' *15)

total = valor
cedula = 50
contced = 0

while True:
    if total >= cedula:
        total -= cedula
        contced += 1
    else:
        if contced > 0:
            print(f'Total de {contced} notas no valor de R${cedula}.')

        if cedula == 50:
            cedula = 20

        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            cedula = 5

        elif cedula == 5:
            cedula = 1

        contced = 0
        if total == 0:
            break

print('==' *15)
print('Transaão concluida com sucesso. Volte sempre!')
