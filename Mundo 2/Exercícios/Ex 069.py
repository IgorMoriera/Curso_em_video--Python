# Exercícios 069 #
#
# Crie um programa que leia a idade e o sexo de várias pessoas. Para cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.


print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 069 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

masc = femin = idadecont = 0

while True:
    print('--' * 15)
    print('     CADASTRE UM PESSOA')
    print('--' * 15)

    idade = int(input('Digite sua idade: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo [M/F]? ')).upper().strip()[0]
    print('=' * 30)
    opcao = ' '

    while opcao not in 'SN':
        opcao = str(input('Você deseja continuar [S/N]? ')).upper().strip()[0]
    print('=' * 30)

    if opcao == 'S':
        # A
        if idade >= 18:
            idadecont += 1
        # B
        if sexo in 'M':
            masc += 1
        # C
        if sexo in 'Ff' and idade < 20:
            femin += 1
    else:
        break

masc += 1
print('-=' * 20)
print(f'''[ A ] - Há {idadecont} pessoas com mais de 18 anos.
[ B ] - Foram cadastrados {masc} homens.
[ C ] - Temos {femin} mulhre(s) com menos de 20 anos de idade cadastradas.''')
print('-=' * 20)
