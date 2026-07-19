# Exercício 124 #
#
# Crie a classe Caneta, que simule o funcionamento de uma caneta colorida, podendo escrever frases na cor relativa.

# Bibliotecas
from rich import print


# ==========================================
# ÁREA DE DECLARAÇÃO DA CLASSE (O Molde)
# ==========================================
class Caneta:
    """

    """

    def __init__(self, cor):
        self.cores = {
            "azul": "blue",
            "vermelha": "red",
            "verde": "green",
            "amarelo": "yellow",
        }

        # 1. Tratamento de Dados: Limpa espaços e joga tudo para minúsculo
        cor_tratada = cor.strip().lower()
        self.cor = self.cores[cor_tratada]
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def quebrar_linha(self, qnt=0):
        for i in range(qnt):
            print("\n" * qnt, end="")

    def escrever(self, texto=""):
        if self.tampada is True:
            print(f"[bold white on red]ATENÇÃO[/]: A caneta [{self.cor}]'{self.cor}'[/] [red]está tampada![/]")

        else:
            print(f"[{self.cor}]{texto}[/]")


# ==========================================
# ÁREA DE DECLARAÇÃO DE OBJETOS (main code)
# ==========================================
c1 = Caneta("Azul")
c2 = Caneta("vermelha")
c3 = Caneta("VERDE")
c4 = Caneta("aMarelo")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Tratando a caneta AZUL")
c1.quebrar_linha(1)
c2.escrever("Tratando a caneta VERMELHA")
c3.escrever("Tratando a caneta VERDE")
c4.escrever("Tratando a caneta AMARELA")
