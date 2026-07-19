# Exercício 120 #
#
# Crie a classe Produto, onde podemos cadastrar nome e preço. Crie também um método etiqueta de preço do produto.


# Impotando algumas bibliotecas
from rich import print
from rich.panel import Panel


# ==========================================
# ÁREA DE DECLARAÇÃO DA CLASSE (O Molde)
# ==========================================
class Produto:
    """

    """

    def __init__(self, nome_produto="", preco=0):
        self.nome_produto  = nome_produto
        self.preco = preco

    def etiqueta(self):
        valorformatado = f"R${self.preco:,.2f}"
        texto = f"""{self.nome_produto:^30}\n{"-" * 30}\n{valorformatado:.^30}"""

        caixa = Panel(f"[white]{texto}[/]", title="Produto", width=34)
        print(caixa)


# ==========================================
# ÁREA DE DECLARAÇÃO DE OBJETOS (main code)
# ==========================================
p1 = Produto("iPhone 17 Pro Max", 25000.85)
p2 = Produto("AppleWatch Series 9", 3200.99)

p1.etiqueta()
p2.etiqueta()
