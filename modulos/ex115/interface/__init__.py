# =========================
# -- Criando a interface
# =========================

# Criação do menu
def cabecalho(txt):
    print('-' * 52)
    print(txt.center(52))
    print('-' * 52)


# Escolhendo uma das opções - Tratando erros
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue

        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar número algum\033[m.')
            return 0

        else:
            return n


# Criado uma interface
def interface(lista):
    cabecalho('MENU PRINCIPAL')
    index = 1

    for opcao in lista:
        print(f'\033[33m{index}\033[m - \033[34m{opcao}\033[m')
        index += 1

    print('-' * 52)
    escolha = leiaInt('\033[33mEscolha uma das opções acima: \033[m')

    return escolha


# Efeito de loading
def loading(qnt=3):
    from time import sleep

    c = 0
    ponto = '.'
    print(f'\033[1;35mLoading{ponto}', end='')
    for c in range(qnt-1):
        sleep(0.5)
        print(f'{ponto}\033[m', end='')
        c += 1
