# ==========================
# -- Manipulando arquivos
# ==========================

from time import sleep
from modulos.ex115.interface import loading


# Verificando se o arquivo existe
def arquivo_Exixte(nome):
    try:
        busca_arquivo = open(nome, 'rt')
        busca_arquivo.close()

    except FileNotFoundError:
        return False

    else:
        return True


# Criando um arquivo
def criando_arquivo(nome):
    try:
        arquivo = open(nome, 'r')
        arquivo.close()
        print('\033[31mJá existe um arquivo com esse nome!\033[m')

    except FileNotFoundError:
        try:
            # Tenta criar o arquivo
            arquivo = open(nome, 'wt+')
            arquivo.close()
            loading()
            sleep(2)

        except:
            print('\033[31mHouve um ERRO na criação do arquivo!\033[m.')

        else:
            print(f'\n\033[1;32mArquivo\033[m \033[m"{nome}"\033[m \033[1;32mcriado com sucesso!\033[m')

    except:
        print('\033[31mHouve um ERRO na verificação do arquivo!\033[m.')


# Lendo um arquivo
def lendo_arquivo(nome):
    try:
        arquivo = open(nome, "rt")

    except:
        print('Erro ao ler arquivo!')

    else:
        print(f'\033[1;34m{'Pessoas':<30}{'Idade':>2}\033[m')
        for linha in arquivo:
            pessoa = linha.split(';')
            pessoa[1] = pessoa[1].replace('\n', '')
            print(f'{pessoa[0]:<30}{pessoa[1]:>2} anos')

    finally:
        arquivo.close()


# Fazendo o cadastro de pessoas no arquivo
def cadastro(nome_arquivo, nome_pessoa='<Desconhecido>', idade=0):

    try:
        arquivo = open(nome_arquivo, 'at')

    except:
        print('\033[31mHouve um ERRO na abertura do arquivo!\033[m.')

    else:
        try:
            arquivo.write(f'{nome_pessoa};{idade}\n')

        except:
            print('\033[31mHouve um ERRO ao registrar os dados!\033[m.')
        else:
            print(f'\033[32m{nome_pessoa}\033[m \033[35mfoi cadastrado(a) com SUCESSO!\033[m.')
            arquivo.close()