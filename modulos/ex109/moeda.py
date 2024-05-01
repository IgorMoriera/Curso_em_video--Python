#========================
# -- Módulos do Ex 109
#========================


def aumentar(n=0, porcentagem=0, formato=False):

    resultado = (n*(porcentagem/100))+n

    if formato is True:
        a = f'R${resultado:.2f}'.replace('.', ',')
        return a

    else:
        return resultado


def diminuir(n=0, porcentagem=0, formato=False):

    resultado = n-(n*(porcentagem/100))

    if formato is True:
        a = f'R${resultado:.2f}'.replace('.', ',')
        return a

    else:
        return resultado


def dobro(n=0, formato=False):

    resultado = n*2

    if formato is True:
        a = f'R${resultado:.2f}'.replace('.', ',')
        return a

    else:
        return resultado


def metade(n=0, formato=False):

    resultado = n/2

    if formato is True:
        a = f'R${resultado:.2f}'.replace('.', ',')
        return a

    return resultado


def formato(n=0, moeda='R$', formatado=False):

    if formatado is True:
        resposta = f'{moeda}{n:.2f}'.replace('.', ',')
        return resposta

    else:
        return n
