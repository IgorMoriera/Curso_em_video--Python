# Estudando os Dicionários

'''


# Declarando um dicinário

    pessoas = {'nome': Igor, 'sexo': 'M', 'idade': 22} ou pessoas = dict()
    print(pessoas) == Imprime o dicionário

    # Nos dicionários não há números como nas listas. Neste caso chamamos a posição pelo nome no lugar da posição.

        pessoas = {'nome': Igor, 'sexo': 'M', 'idade': 22}

        * print(pessoas['nome']) -- Retorna o valor atribuido à posição 'nome', neste caso: Igor
        * print(pessoas['sexo']) -- Retorna o valor atribuido à posição 'sexo', neste caso: M
        * print(pessoas['idade']) -- Retorna o valor atribuido à posição 'idade', neste caso: 22


# Exibindo os valores dos dicionários na tela

    pessoas = {'nome': Igor, 'sexo': 'M', 'idade': 22}
    print(f'O {pessoas["nome"]} tem {pessoas["idade"] anos.'} -- UTILIZAR ASPAS DUPLA DENTRO DO ARGUMENTO DO DIC.


# Função do dicionário

    * Keys -- Retorna as chaves do dicionário

        pessoas = {'nome': Igor, 'sexo': 'M', 'idade': 22}
        print(pessoas.Keys()) -- 'nome', 'sexo' e 'idade'


    * values -- Retorna os valores atribuidos às chaves

        pessoas = {'nome': Igor, 'sexo': 'M', 'idade': 22}
        print(pessoas.Keys()) -- 'Igor', 'M' e 22


    * items -- Retorna uma composição de elementos (uma lista composta de tuplas)

        pessoas = {'nome': Igor, 'sexo': 'M', 'idade': 22}
        print(pessoas.Keys()) -- dict_items([('nome', 'Igor'), ('sexo', 'M'), ('idade', 22)])


# Acessando valores das Keys, values e items com loopings

    # lendo as Keys:

        pessoas = {'nome': Igor, 'sexo': 'M', 'idade': 22}
        for k in pessoas.Keys():
            print(k) -- nome... sexo... idade...


    # lendo as values:

        pessoas = {'nome': Igor, 'sexo': 'M', 'idade': 22}
        for v in pessoas.values():
            print(v) -- Igor... M...22


    # lendo os items -- necessário utilizar duas variáveis para jogar os valores de items na tela

        pessoas = {'nome': Igor, 'sexo': 'M', 'idade': 22}
        for k, v in pessoas.items():
            print(f'{k} = {v}') -- nome = Igor ... Sexo = M ... Idade = 22


# Apagando, atribuindo ou adicionando elementos

   * Apagando

        pessoas = {'nome': Igor, 'sexo': 'M', 'idade': 22}
        del pessoas['sexo']
            for k, v in pessoas.values():
                print(f'{k} = {v}') -- nome = Igor ... Idade = 22

   * Atribuindo

        pessoas = {'nome': Igor, 'sexo': 'M', 'idade': 22}
        del pessoas['nome'] = 'Leandro
            for k, v in pessoas.values():
                print(f'{k} = {v}') -- nome = Leandro ... Sexo: M ... Idade = 22


   * Atribuindo

        pessoas = {'nome': Igor, 'sexo': 'M', 'idade': 22}
        del pessoas['peso'] = 98,5
            for k, v in pessoas.values():
                print(f'{k} = {v}') -- nome = Leandro ... Sexo: M ... Idade = 22 ... Peso = 98,5


# Criando dicionários dentro de listas

    brasil = []
    estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
    estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
    brasil.append(estado1)
    brasil.append(estado2)

    print(brasil) -- [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]

   * Identificando os itens da lista (devolvendo os dicionários):

        print(brasil[0]) -- {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
        print(brasil[1]) -- {'uf': 'São Paulo', 'sigla': 'SP'}

   * Identificando os itens dos dicionários nas listas (devolvendo os itens dos dicionários):

        print(brasil[0]['uf']) -- Rio de Janeiro
        print(brasil[1]['sigla']) -- SP


# Atribuindo valores aos diconários -- utilizando a função copy()

    estado = dict()
    brasil = list()
    for c in range(0, 3):
        estado['uf'] = str(input('Unidade Federativa: '))
        estado['sigla'] = str(input('Sigla do estado: '))
        brasil.append(estado.copy())
        print(brasil)

    for e in brasil:
        for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

ou

    for e in brasil:
        for v in e.items():
            print(v, end=' ')
        print()











'''
