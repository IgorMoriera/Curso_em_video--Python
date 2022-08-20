# Estudando as listas - Parte 1
'''
Lista - num [2 , 5, 9, 1] - utiliza  parêntses.

===== LISTAS SÃO MUTÁVEIS =====

num = [2 , 5, 9, 1]

# Alterando uma lista:

    num[2] = 3 - número na poição 2 da lista recebe o núm 2.


# Adicionando um valor na lista:

    num.append(7) - adiciona o número 7 na última posição da lista
    print(num) - num = [2 , 5, 9, 1, 7]


# Colocando os números das listas em ordem crescente e decrescente

    num.sort() - coloca a lista em ordem
    num.sort(reverse=True) - mostrando em ordem decrescente



# Mostrando a qnt de itens em uma lista

    print(len(num))



# Inserindo valores nas listas

    num.insert(2, 0) - inserindo o núm 2 na posição 0 da lista.
    num.insert(2, 2) -   ||        ||         ||    2 da lista



# removendo um elemento da lista

    num.pop() - elimina o último número da lista
    num.pop(2) - elimina o elemento da segunda posição

OU

    num.remove(2) - remove apenas o primeiro elemento da lista desejado.
    num.remove(4) - se tentar remover um valor que não está na lista, a IDE apresenta um erro.

    Para resolver esse erro podemos fazer:
        if 4 in num:
            num.remove(4) - remove o num 4
        else:
            print(f'Essa lista não possui o número 4') - não remove o num 4



# Começndo uma lista

    valores = []   ou valores = list()



# Mostrando valores de uma lista

    valores = [] - lista vazia
    valores.append(5) - Adicionando valores na lista
    valores.append(9)
    valores.append(4)

    for v in valores:
        print(f'{v}...', end=' ') - 5...9...4...



# Mostrando os valores em suas respectivas posições na lista

    valores = [] - lista vazia (se a IDE reclamar, colocar o list()
    valores.append(5) - Adicionando valores na lista
    valores.append(9)
    valores.append(4)

    for c, v in enumerate(valores):
        print(f'Na posição {c} encontrei o valor {v}!')
    print('Fim da lista')



# lendo valores e add nas listas pelo teclado

    valores = list()

    for cont in range(0, 5) - contando 5 valores
        valores.append(int(input('Diite um valor: '))) - Lendo 5 valores pelo usuário e add em uma lista




# Copiando uma lista

    a = [2, 3, 4, 8]
        b = a[:] - DESSA FORMA EU COLOCO TODOS OS VALORES DE a EM b. (CRIANDO UMA CÓPIA DE A P/ B)
        b[2] = 7 - add o núm 7 ba posição 2

# OBS:
        a = [2, 3, 4, 8]
        b = a - DESSA FORMA ESTOU FAZENDO UMA LIGAÇÃO ENTRE AS LISTAS
        b[2] = 7 - add o núm 7 ba posição 2
        O resltdo é que o python add o valor 7 tanto na lista A, uanto na B.
'''
