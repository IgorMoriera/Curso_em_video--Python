print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 097 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

def escreva(msg):
    tam = len(f'  {msg}') + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa principal
a = str((input('Digite uma frase: ')))
escreva(a)
