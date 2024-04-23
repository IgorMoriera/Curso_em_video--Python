# Exercício 097 #
#
# Crie um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
#  mensagem com tamanho adaptaível.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 097 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

def escreva():

    msg = str(input('Digite uma frase: '))
    tam = len(f'  {msg}') + 2
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa principal
escreva()
