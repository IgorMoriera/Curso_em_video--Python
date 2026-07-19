# Exercício 121 #
#
# Creia a classe Churrasco, onde seja possível infomrar quantas pessoas vão participar e quanto de carne deve
# ser comprado, o custo total do churasco e o preço por pessoa.
# Considerar: consume de 400g de carne/pessoa e preço ed R$82.40/Kg


# Bibliotecas
from rich import print
from rich.panel import Panel


# ==========================================
# ÁREA DE DECLARAÇÃO DA CLASSE (O Molde)
# ==========================================
class Churrasco:
    """

    """

    def __init__(self, titulo="", qnt_pessoas=0):
        self.titulo = titulo
        self.qnt    = qnt_pessoas
        self.valo_kg = 82.4
        self.qnt_carne_pessoa = 0.4

    def analisar(self):

        # Cálculos
        qnt_total_carne = self.qnt * self.qnt_carne_pessoa
        custo_total = qnt_total_carne * self.valo_kg
        valor_por_pessoa = custo_total / self.qnt

        texto = f"""> Analisando o [green]{self.titulo}[/] com {self.qnt} convidados
1. Cada participante comerá 0.4Kg e cada Kg de carne custa R$82.4
2. Recomendo [blue]comprar {qnt_total_carne:.2f}kg[/] de carne
3. O custo total será de [red]R${custo_total:.2f}[/]
4. Cada pessoa pagará [green]R${valor_por_pessoa:.2f}[/] para participar."""

        caixa = Panel(f"[white]{texto}[/]", title=self.titulo)

        return print(caixa)


# ==========================================
# ÁREA DE DECLARAÇÃO DE OBJETOS (main code)
# ==========================================
c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()
