# Exercício 089 #
#
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
# um boletim cotendo a média de cada um e permita que o usuário possta mostrar as notas de cada aluno individualmente.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 089 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

sala = list()

notaum = notadois = toal = 0
while True:
    # Add o nome em uma lista
    nome = str(input('Digite o nome do aluno: ')).strip()

    # Add as notas e calculando a média
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    # Add os nomes + as notas em uma terceira e última lista
    sala.append([nome, [nota1, nota2], media])

    resposta = str(input('Continuar? [S/N] ')).strip().upper()
    while resposta not in 'SN':
        print('Opção incorreta! Tente novamente.')
        resposta = str(input('Continuar? [S/N] ')).strip().upper()

    if resposta == 'N':
        break

print('-=' * 30)
print(f'{"Nº":<5}{"NOMES":<10}{"MÉDIAS":>9}')
print('--' * 20 )

for i, c in enumerate(sala):
    print(f"{i:<5}{c[0]:<10}{c[2]:>8.1f}")

while True:
    print('--' * 30)
    opcao = int(input('Notas de qual aluno você que visualizar? (999 para sair): '))

    if opcao == 999:
        print('\nFINALIZADO...')
        break

    if opcao <= len(sala) - 1:
        print(f'As notas de {sala[opcao][0]} froam: {sala[opcao][1]}')
