# Estudando Funções part 2

#>> Interative Help - ajuda interativa

    '''
    Para obter a ajuda interativa, basta digitar: help()
e em seguida digitar o nome do comando desejado para verificar todas as infomações do comando escolhido.

    EX: help()
    '''

#>> Docstrings - manual do comando desejado

    #Esta função retorna o que significa os parâmetros de cada função escolhida.

    #EX:
        def contador(i, f, p):
            '''
                -> Faz uma contagem e mostra na tela.
                :param i: início da contagem
                :param f: fim da contagem
                :param p: passo da contagem
                :return: sem retorno
            '''
            c = i
            while c <= f:
                print(f'{c}', end='..')
                c += p
            print('FIM!')

        contador(0, 100, 10)
    help(contador)


#>> Parâmetros opcionais

    #EX:
        def contador(a=0, b=0, c=0):
            s = a + b + c
            print(f'A soma vale {s}')
        somar(3, 3, 5)
        somar(6, 5)
        somar(6)




>> Escopo de variáveis

    >>>> - '''Descrição deste assunto resumido em foto salva nos arquivos do curso.'''



>> Retorno de resultados

    O comando "return..." após concluir a 1º verificação da função, retorna atribui seu valor à umadeterminada variável.

    EX:
        def contador(a=0, b=0, c=0):
            s = a + b + c
            return s

        r1 = somar(3, 3, 5)
        r2 = somar(6, 5)
        r3 = somar(5)
        print(f'Meus resultados deram {r1}, {r2} e {r3}')



# Exemplo compilando a matéria acima:

    >> 'Realizando o fatorial de um número'

    def fatorial(num=1):
        f = 1
        for c in range(num, 0, -1):
            f *+ c
        return f

    f1 = fatorial(5)
    f2 = fatorial(4)
    f3 = fatorial()
    print(f'Os resultados foram {f1}, {f2} e {f3}')



    >> 'Verificando se o num é ou não PAR'

    def par(n=0):
        if n % 2 == 0:
            return True
        else:
            return False

    num = int(input('Digite um número: '))
    if par(num):
        print('É par!')
    else:
        print('Não é par!')
