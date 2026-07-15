# Exercício 115 #
#
# Crie um sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from modulos.ex115.interface import *
from modulos.ex115.arquivo import *

# Variável que nomeia o arquivo de cadastro
nome_arquivo = 'Cadastro_pessoas.txt'

while True:
    escolhendo_opcao = interface(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa',
                                 'Criando um novo arquivo', 'Sair do Sistema'])

    if escolhendo_opcao == 1:
        cabecalho('PESSOAS CADASTRADAS')

        if arquivo_Exixte(nome_arquivo) is False:
            print('\033[1;31mATENÇÃO!\033[m')
            print(' > Utilize a \033[1;31mOpção 3\033[m para criar um arquivo.')

        else:
            lendo_arquivo(nome_arquivo)

# ------------------------------------------------------------
    elif escolhendo_opcao == 2:
        cabecalho('NOVO CADASTRO')
        nome_pessoa = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastro(nome_arquivo, nome_pessoa, idade)

# ------------------------------------------------------------
    elif escolhendo_opcao == 3:
        cabecalho('CRIANDO UM NOVO ARQUIVO')
        criando_arquivo(nome_arquivo)

# ------------------------------------------------------------
    elif escolhendo_opcao == 4:
        cabecalho('\033[1;31mSaindo do sistema...\033[m \033[1;32mAté logo!\033[m')
        break

    else:
        print('\033[0;31mERRO! Digite uma das opções válidas!\033[m.')
