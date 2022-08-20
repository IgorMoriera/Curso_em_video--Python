# Estudando as Tuplas

'''Utilizamos () para representar as tuplas (não é obrigatório)

Exemplos:

# Repreentando uma tupla:

  =================================
  ===== TUPLAS SÃO IMUTÁVEIS ======
  =================================

    lanche = ('Hamburuer', 'Suco', 'Pizza', 'Pudim')
    print(lanche)

# sendo assim temos:
lanche = ('Hamburuer', 'Suco', 'Pizza', 'Pudim')
print(lanche[0]) = Hamburguer
print(lanche[1]) = Suco
print(lanche[2]) = Pizza
print(lanche[3]) = Pudim

# ou temos
lanche = ('Hamburuer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-4]) = Hamburguer
print(lanche[-3]) = Suco
print(lanche[-2]) = Pizza
print(lanche[-1]) = Pudim

# Podemos fatiar as tuplas utilizando os seguintes comandos:

    # Mostrando do termo 1 até o 3 -> mostra termo 1, 2 e desconsidera o 3.
    lanche = ('Hamburuer', 'Suco', 'Pizza', 'Pudim')
    print(lanche[1:3])

    # Mostrando de um elemento até o final:
    lanche = ('Hamburuer', 'Suco', 'Pizza', 'Pudim')
    print(lanche[2:])  ou  print(lanche[:2]) # Desconsidera o termo 2 neste caso.

# Mostrando itens das tuplas sem parenteses e aspas...

    # 1ª Ex
        for comida in lanche:
            print(f'EU VOU COMER {comida}')
        print('Comi pra caramba!')

# Utilizando a função len()
print(len(lanche))

    # 2ª Ex
        for cont in range(0, len(lanche)): # Mostra de 0 até (n-1) a qnt. de termos pressentes na tupla, desconsiderando o ultimo item.
            print(f'EU VOU COMER {comida}')
        print('Comi pra caramba!')

    # Ex 2.1
        # Mostrando os itens ao invés dos números:
        for cont in range(0, len(lanche)):  # Mostra de 0 até (n-1) a qnt. de termos pressentes na tupla, desconsiderando o ultimo item.
                print(f'EU VOU COMER {lanche(cont)}')
        print('Comi pra caramba!')

    # Ex 3
        for cont in range(0, len(lanche)):  # Mostra de 0 até (n-1) a qnt. de termos pressentes na tupla, desconsiderando o ultimo item e a posição de cada item.
                print(f'EU VOU COMER {lanche(cont)} na posição {cont}')
        print('Comi pra caramba!')

    # Ex 3.1
    # Função enumerate: funciona igual o ex 3 acima.
        for posicao, comida in enumerate(lanche):  # Mostra de 0 até (n-1) a qnt. de termos pressentes na tupla, desconsiderando o ultimo item e a posição de cada item.
            print(f'EU VOU COMER {comida} na posição {posicao}')
        print('Comi pra caramba!')


# Funcao sorted()
    # Coloca os itens em ordem alfábetica

        lanche = ('Hamburuer', 'Suco', 'Pizza', 'Pudim')
        print(sorted(lanche))


# "Soma" de tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b   ->   c = (2, 5, 4, 5, 8, 1, 2)

# Contando itens que se repete:
print(c.count(5)) # quantas vees aparece o número 5 dentro da tupula.

# Prorpiedade index () retorna a posição de um termo escolhido pertecente a tupla
print(c.index(4)) # O num 4 está na posição 2.


# Apagando um variável
lanche =  = ('Hamburuer', 'Suco', 'Pizza', 'Pudim')
del(lanche) # deleta a tuplas inteira. não é possível excluir apenas um item.'''