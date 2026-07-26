# Exercício 125 #
#
# Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle simples (canal, volume, liga/desliga)

# Bibliotecas
import os
from rich import print
from rich.panel import Panel


# ==========================================
# ÁREA DE DECLARAÇÃO DA CLASSE (O Molde)
# ==========================================
class ControleRemoto:
    """

    """

    canal_min = 1
    canal_max = 5
    volume_min = 0
    volume_max = 10

    def __init__(self):
        self.tv_ligada = False
        self.canal_atual = ControleRemoto.canal_min
        self.volume_atual = 2

    def power(self):
        self.tv_ligada = not self.tv_ligada

    def tv_desligada(self):
        texto = f"[red]A TV está DESLIGADA![/]"
        caixa = Panel(f"{texto}", title="[ TV ]", width=25)
        print(caixa)

    def volume_mais(self):
        if self.tv_ligada:
            if self.volume_atual < ControleRemoto.volume_max:
                self.volume_atual += 1
        else:
            self.tv_desligada()

    def volume_menos(self):
        if self.tv_ligada:
            if self.volume_atual > ControleRemoto.volume_min:
                self.volume_atual -= 1
        else:
            self.tv_desligada()

    def subir_canal(self):
        if self.tv_ligada:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1
        else:
            self.tv_desligada()

    def descer_canal(self):
        if self.tv_ligada:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1
        else:
            self.tv_desligada()

    def mostrar_painel(self):
        if not self.tv_ligada:
            caixa = Panel("[red]A TV está DESLIGADA[/]", title="[ TV ]", width=35)
            print(caixa)

        else:
            # 1. Montando a linha dos Canais
            str_canais = ""

            for c in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):  # Canais de 1 a 5
                if c == self.canal_atual:
                    str_canais += f"[black on yellow] {c} [/] "
                else:
                    str_canais += f"{c} "

            # 2. Montando os Blocos de Volume
            str_volume = ("[cyan]█[/]" * self.volume_atual) + ("[grey50]█[/]" * (10 - self.volume_atual))

            # 3. Juntando tudo no Painel
            texto_tela = f"CANAL  = {str_canais}\nVOLUME = {str_volume}"
            caixa = Panel(texto_tela, title="[ TV ]", width=35)
            print(caixa)

    def minhatv(self):
        while True:
            # 1. Limpa o terminal
            os.system('cls' if os.name == 'nt' else 'clear')

            # 2. Chama o método que imprime o painel da TV
            self.mostrar_painel()

            # 3. Pede o input do usuário
            comando = input("On/Off: @ | < CH > | - VOL + | ").strip().lower()

            # 4. Roteador de Comandos
            if comando == '0':
                break  # Sai do programa

            elif comando == '@':
                self.power()

            elif comando == '+':
                self.volume_mais()

            elif comando == '-':
                self.volume_menos()

            elif comando == '>':
                self.subir_canal()

            elif comando == '<':
                self.descer_canal()


# ==========================================
# ÁREA DE DECLARAÇÃO DE OBJETOS (main code)
# ==========================================
# Instancia a sua TV
tv = ControleRemoto()
tv.minhatv()
