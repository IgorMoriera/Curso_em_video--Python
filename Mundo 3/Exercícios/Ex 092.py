print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 092 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

from datetime import date
hoje = date.today().year
pessoa = dict()

pessoa['Nome'] = str(input('Nome: ')).strip()

ano = int(input('Ano de Nascimento: '))
idade = hoje - ano
pessoa['Idade'] = idade

pessoa['CTPS'] = int(input('Carteira de trabalho (0 se nãotiver): '))

if pessoa['CTPS'] == 0:
    print('-=' * 25)

    for k, v in pessoa.items():
        print(f'{k}: {v}')

else:
    pessoa['Salário'] = float(input('Digite seu salário: R$'))

    ano_contratacao = int(input('Ano de Contratação: '))
    aposentar = ano_contratacao + 35
    pessoa['Aposentadoria'] = aposentar

    print('-=' * 25)

    for k, v in pessoa.items():
        print(f'{k}: {v}')
