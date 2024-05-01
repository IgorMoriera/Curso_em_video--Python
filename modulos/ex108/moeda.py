#========================
# -- Módulos do Ex 108
#========================


def aumentar(n=0, porcentagem=0):
    a = (n*(porcentagem/100))+n
    return a


def diminuir(n=0, porcentagem=0):
    a = n-(n*(porcentagem/100))
    return a


def dobro(n=0):
    a = n*2
    return a


def metade(n=0):
    a = n/2
    return a


def formato(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

