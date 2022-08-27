# Exercício 020 #
#
# O mesmo professor do desafio anterior quer sortear a ordem de uma apresentação de trabalhos dos alunos.
#  Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 020 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Importando a função  'random' [Aleatório]
import random

# Definindo o nome dos alunos
A = str(input('1º Grupo: '))
B = str(input('2º Grupo: '))
C = str(input('3º Grupo: '))
D = str(input('4º Grupo: '))

# Atrbuindo os nomes em uma lista
lista = [A, B, C, D]

# Escolhendo aleatóriamente um dos nomes inseridos
random.shuffle(lista)

# Mostrando na tela o aluno sorteado
print('A sequência das apresentações é: {}'.format(lista))
