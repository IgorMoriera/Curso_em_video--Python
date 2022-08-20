# Estudando Funções part 1

'''
def é dedefinição de função:

# Definindo uma função para SOMA
    def soma(a, b):
        s = a + b
        print(s)

    soma(4, 5) -- 9   ou soma(a=4, b=5)
    soma(8, 9) -- 17
    soma(2, 1) -- 3


# Função de desempacotamento de parâmetros

    # Definindo o empacotador como: def contador(* num):

    def contador(* num):
        for valor in num:
            print(f"{valor} ", end='')
        print('FIM!')


    contador(2, 1, 7)       -- 2 1 7 FIM!
    contador(8, 0)          -- 8 0 FIM!
    contador(4, 4, 7, 6, 2) -- 4 4 7 6 2 FIM!



    # Fazendo um somador com vários númeoros:

        def soma(* valores):
            s = 0
            for num in valores:
                s += num
            print(f'Somando os valores {valores} temos {s}')

        soma(5, 2)      -- 7
        soma(2, 9, 4)   -- 15



    # Fazendo um contador

        def contador(* num):
            tam = len(num)
            print(f'Recebi os valores {num} e são aotodo {tam} números')

        contador(2, 1, 7)       -- ... e são aotodo 3 números
        contador(8, 0)          -- ... e são aotodo 2 números
        contador(4, 4, 7, 6, 2) -- ...e são aotodo 5 números



# Trabalhando com as listas como funções

    # Dobradno valores em uma lista

        def dobra(lst):
            pos = 0
            while pos < len(lst):
                lst[pos] *= 2
                pos += 1

        valores = [6, 3, 9, 1, 0, 2]
        dobra(valores)
        print(valores) -- [12, 18, 2, 0, 4]

'''