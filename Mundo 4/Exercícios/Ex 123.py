# Exercício 123 #
#
# Crie a classe Gamer, onde podemos cadastrar nome, nick e jogos favoritos de uma pessoa. Crie um método que também
# permita mostrar a ficha desse gamer.


# Bibliotecas
from rich import print
from rich.panel import Panel


# ==========================================
# ÁREA DE DECLARAÇÃO DA CLASSE (O Molde)
# ==========================================
class Gamer:
    """

    """

    def __init__(self, nome_jogador="", nick=""):
        self.nome_jogador = nome_jogador
        self.nick = nick
        self.jogos_favoritos = []

    def add_favoritos(self, nome_jogo_cadastrado=""):
        self.jogos_favoritos.append(nome_jogo_cadastrado)

    def ficha(self):
        texto = f"Nome real: [bold white on blue]{self.nome_jogador}[/]\nJogos favoritos:\n"
        for i in sorted(self.jogos_favoritos):
            texto += f" > [blue]{i}[/]\n"

        caixa = Panel(texto, title=f"Jogador <{self.nick}>", width=40)
        print(caixa)


# ==========================================
# ÁREA DE DECLARAÇÃO DE OBJETOS (main code)
# ==========================================
j1 = Gamer("Igor Moreira", "Mike")
j1.add_favoritos("Dante's Inferno")
j1.add_favoritos("GTA VI")
j1.add_favoritos("God of War")
j1.add_favoritos("COD")
j1.ficha()

j2 = Gamer("Arya", "Aryana")
j2.add_favoritos("Sonic")
j2.add_favoritos("Fortnite")
j2.ficha()

