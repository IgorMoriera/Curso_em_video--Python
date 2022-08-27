# Exercício 019 #
#
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#  Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 019 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Lendo o nome dos alunos da turma de 4 alunos
nome_1 = str(input('1º Aluno: '))
nome_2 = str(input('2º Aluno: '))
nome_3 = str(input('3º Aluno: '))
nome_4 = str(input('4º Aluno: '))

# Montando uma lista com o nome de todos os alunos
lista = [nome_1, nome_2, nome_3, nome_4]

# Importando a função 'random' [aleatório]
import random

# Mostrando na tela o nome do aluno escolhido para apagar o quadro
print('O aluno(a) sorteado(a) para apagar o quadro é o(a): {}'.format(random.choice(lista)))
