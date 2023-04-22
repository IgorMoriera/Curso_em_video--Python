# Exercício 079 #
#
# Crie um programa onde usuário possa digitar vários valores numéricos e cadasrte-os em uma lsita. Caso o números já
# exista lá dentro, ele não será adiconado. No final, serão exibidos todos os valores numéricos digitados
# em ordem crescente.


print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 079 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

num = list()

while True:
    n = (int(input('Digite um valor: ')))
    if n not in num:
        num.append(n)
        num.sort()
        print('Valor adicionado com sucesso!')
    else:
        print('Este valor já está na lista. Não vou adicionar.')

    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()

    while resposta not in 'SsNn':
        resposta = str(input('Resposta incorreta! Tente novamente. \nDeseja continuar? [S/N] ')).strip().upper()

    if resposta == 'N':
        break

print('-=' * 25)
print(f'Você digitou os valores: {num}')
