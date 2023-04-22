# Exercício 080 #
#
# Crie um proigrama onde o usuário possa digitar 5 valores numéricos e cadastr-os em uma lista, já na posição correta
# de inserção (sem utilizar o sort()).
# No final, mostre a lsita ordenada na tela.


print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 080 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

lista = list()

for cont in range(0, 5):
    num = int(input(f'Digite um valor: '))

    if cont == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado no final da lista...')
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1

print('-=' * 20)
print(f'Você digitou os números: {lista}')
