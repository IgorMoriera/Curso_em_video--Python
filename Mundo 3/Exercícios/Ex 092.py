# Exercício 092 #
#
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário recebera também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 092 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

from datetime import date
hoje = date.today().year
pessoa = dict()

pessoa['Nome'] = str(input('Nome: ')).strip()

ano = int(input('Ano de Nascimento: '))
pessoa['Idade'] = hoje - ano
pessoa['CTPS'] = int(input('Carteira de trabalho (0 se não tiver): '))

if pessoa['CTPS'] == 0:
    print('-=' * 25)

    for k, v in pessoa.items():
        print(f'{k}: {v}')

else:
    pessoa['Salário'] = float(input('Digite seu salário: R$'))

    ano_contratacao = int(input('Ano de Contratação: '))
    pessoa['Aposentadoria'] = ano_contratacao + 35

    print('-=' * 25)

    for k, v in pessoa.items():
        print(f'{k}: {v}')
