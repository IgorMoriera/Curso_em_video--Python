# Estudando as listas - Parte 2

'''

# criando uma lista e inserindo dados com o 'append' na lista
    # Mesma forma vista na aula 17

    teste = list()
    teste.append('Gustavo')
    teste.append(40)
    print(teste)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Mostrando uma lista dentrio de outra lista

    teste = list()
    teste.append('Gustavo')
    teste.append(40)

        ## Inserindo o comando abaixo consegue-se inserir a lista 'teste' dentro da lista 'galera'
    galera = list()
    galera.append(teste)
    print(galera) ------- Resultado do print: [['Gustavo', 40]]

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Fazendo a cópia de ma lista para outra lista

    teste = list()
    teste.append('Gustavo')
    teste.append(40)
    galera = list()
            ## Inserindo o comando 'galera.append(teste[:])' estou gerando uma cópia dos dados contidos em 'teste'
    galera.append(teste[:])
    teste[0] = 'Marcia'
    teste[1] = 22
    galera.append(teste[:])

    print(galera) ------- Resultado do print: [['Gustavo', 40], ['Maria', 22]]

            ## Caso não tenha feito uma cópiao resultado é o mesmo dos dados já existentes como abaixo:
                    print(galera) ------- Resultado do print: [['Gustavo', 40], ['Gustavo', 40]]

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Criando uma lista dentro de outra lista

    galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

    # Mostrnado valores da lista GALERA

        # Retornando todos os dados da 1º posição

            print(galera[0]) == Retorna: ['João', 19]

        # Retornando o 1º item da 2º lista (nome do participante)

                print(galera[0][0]) == Retorna: João
                print(galera[2][1]) == Retorna: 13 (idade do Joaquim)

# Exibindo todos os dados de uma lista composta

    galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
    for p in galera:

    print(p) -- Retornando todos os valores da lista 'galera'

    # Mostrando apeans os * nomes * de cada pessoa da lista galera

       galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
       for p in galera:

            # Para isso add '[0]' -- primeiro item de cada sublista dentro de 'galera'
            # Caso coloque '[1]' é exibido a idade -- segundo item de cada sublista

       print(p[0]) -- Retornando todos os valores da lista 'galera'

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Inserindo dados em uma sublistas contida em uma lista

    galera = list() -- Lista principal
    dado = list()   -- Sublista
    totmai = totmen = 0

    for c in range(0, 3):
        dado.append(str(input('Nome: ')))     -- inserindo o nome
        dado.append(int(input('Idade: ')))    -- inserindo aa idade
        galera.append(dado[:])      -- copiando as informações de dados --> galera
        dados.clear() -- li mpando os dados na próxima execução do programa

    # Mostrnado as pessoas masi velhas da lista galera...

    for p in galera:
        if p[1] >= 21:
            print(f'{p[0]} é o maior de idade.')
            totmai += 1

        else:
            print(f'{p[0]} é o menor de idade.')
            totmen += 1

    print(f'Temos {totmai} maiores e {totmen} menores de idade.')









'''