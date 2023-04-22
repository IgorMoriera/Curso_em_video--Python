# Exercício 077 #
#
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais sãocsuas vogais.


print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 077 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

palavras = ('PALAVRAS', 'CARNAGUEIJO', 'BOB', 'ESTANTE', 'MARVEL', 'PEAO', 'PARALELEPIPEDO', 'EVENTO', 'NOITADA',
            'PRESUNTO', 'QUEIJO', 'CARNE', 'HAMBURGUERR', 'ELA', 'ARREPIO')

for c in palavras:
    print(f'\nPara a palavra {c} temos: ', end=' ')
    for letras in c:
        if letras.lower() in 'aeiou':
            print(letras.lower(), end=' ')
