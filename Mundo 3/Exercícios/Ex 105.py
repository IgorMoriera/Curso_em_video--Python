# Exercício 105 #
#
# Crie um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com
#  as seguintes informações:
#
#  - Quantidade de notas
#  - A maior nota
#  - A menor nota
#  - A média da turma
#  - A situação (opcional)
#
# Adicione também as docstrings da função.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 105 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)


def notas(*num, situacao=False):
    """
    --> Função para analisar notas e situação de vários alunos.
        > parâmetro num: uma ou mais notas dos alunos (aceitar várias).
        > parâmetro situacao: Valor opcional, indicado se deve ou não adiconar a situação.
        > return: Dicionário com várias informações sobre a situação de turma.
    """

    total_notas = {}
    total_notas['Qtd. Notas'] = len(num)
    total_notas['Maior nota'] = max(num)
    total_notas['Menor nota'] = min(num)
    total_notas['Média da turma'] = sum(num) / len(num)
    if sit is True:
        if total_notas['Média da turma'] >= 7:
            total_notas['Situação'] = 'BOA'

        elif total_notas['Média da turma'] >= 5:
            total_notas['Situação'] = 'RAZOÁVEL'

        else:
            total_notas['Situação'] = 'RUIM'

    return total_notas


# Programa principal
resp = notas(7, 10, 6.5, situacao=True)
print(resp)
