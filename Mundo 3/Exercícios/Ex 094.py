# Exercício 094 #
#
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dadps de cada ésspa em um dicionário e
#  todos os dicionários em uma lista.

# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista com todas as pessoas com idades acima da média.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 094 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

grupo = list()
pessoa = dict()

cont = soma = 0

while True:
    pessoa['Nome'] = str(input('Nome: ')).strip()

    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()

        if pessoa['Sexo'] in 'MF':
            break
        print('Erro! Por favor, digite M ou F.')

    pessoa['Idade'] = int(input('Idade: '))

    soma += pessoa['Idade']
    cont += 1

    grupo.append(pessoa.copy())
    pessoa.clear()

    resposta = str(input('Quer continuar? [S/N] ')).upper().upper()

    while resposta not in 'SN':
        print('Erro! Por favor, responda apenas S ou N.')
        resposta = str(input('Quer continuar? [S/N] ')).upper().upper()

    if resposta == 'N':
        break

print('-=' * 30)
print(f'[ A ] - O grupo tem {cont} pessoas.')
print(f'[ B ] - A média de idade é de {soma/cont:5.2f} anos.')

print('[ C ] - As mulheres cadastradas foram: ', end='')
for m in grupo:
    if m['Sexo'] == 'F':
        print(f'{m["Nome"]}...', end='')
print()

print('[ D ] - Lista de pessoas que estão acima da média: ', end='')
for p in grupo:
    if p['Idade'] >= (soma/cont):
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()

print('\n<<< ENCERRADO >>>')
