# ========================
# -- Módulos do Ex 112
# ========================


def aumentar(n=0, porcentagem=0, formato=False):
    resultado = (n * (porcentagem / 100)) + n
    return resultado if formato is False else moeda(resultado)


def diminuir(n=0, porcentagem=0, formato=False):
    resultado = n - (n * (porcentagem / 100))
    return resultado if formato is False else moeda(resultado)


def dobro(n=0, formato=False):
    resultado = n * 2
    return resultado if not formato else moeda(resultado)


def metade(n=0, formato=False):
    resultado = n / 2
    return resultado if not formato else moeda(resultado)


def moeda(n=0, cambio='R$'):
    resposta = f'{cambio}{n:.2f}'.replace('.', ',')
    return resposta


def resumo(n=0, aumento=10, reducao=5):

    print('-'*30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-'*30)

    print(f'Preço analisado:   {moeda(n)}\n'
          f'Dobro do preço:    {dobro(n, True)}\n'
          f'Metade do preço:   {metade(n, True)}\n'
          f'{aumento}% de aumento:    {aumentar(n, aumento, formato=True)}\n'
          f'{reducao}% de redução:    {diminuir(n, reducao, formato=True)}'
          )

    print('-' * 30)
