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

    def __init__(self):
        self.tv_ligada = False
        self.canal = 1
        self.volume = 2

    def power(self):
        self.tv_ligada = not self.tv_ligada

    def volume_mais(self):
        if self.tv_ligada is True:
            if self.volume < 10:
                self.volume += 1
        else:
            texto = f"[red]A TV está DESLIGADA![/]"
            caixa = Panel(f"{texto}", title="[ TV ]", width=25)
            print(caixa)

    def volume_menos(self):
        if self.tv_ligada is True:
            if self.volume > 0:
                self.volume -= 1
        else:
            texto = f"[red]A TV está DESLIGADA![/]"
            caixa = Panel(f"{texto}", title="[ TV ]", width=25)
            print(caixa)

    def subir_canal(self):
        if self.tv_ligada is True:
            if self.canal < 5:
                self.canal += 1
        else:
            texto = f"[red]A TV está DESLIGADA![/]"
            caixa = Panel(f"{texto}", title="[ TV ]", width=25)
            print(caixa)

    def descer_canal(self):
        if self.tv_ligada is True:
            if self.canal > 0:
                self.canal -= 1
        else:
            texto = f"[red]A TV está DESLIGADA![/]"
            caixa = Panel(f"{texto}", title="[ TV ]", width=25)
            print(caixa)

    def mostrar_painel(self):
        if not self.tv_ligada:
            caixa = Panel("[red]A TV está DESLIGADA[/]", title="[ TV ]", width=35)
            print(caixa)

        else:
            # 1. Montando a linha dos Canais
            str_canais = ""
            for c in range(1, 6):  # Canais de 1 a 5
                if c == self.canal:
                    str_canais += f"[black on yellow] {c} [/] "
                else:
                    str_canais += f"{c} "

            # 2. Montando os Blocos de Volume
            str_volume = ("[cyan]█[/]" * self.volume) + ("[grey50]█[/]" * (10 - self.volume))

            # 3. Juntando tudo no Painel
            texto_tela = f"CANAL  = {str_canais}\nVOLUME = {str_volume}"
            caixa = Panel(texto_tela, title="[ TV ]", width=35)
            print(caixa)


# ==========================================
# ÁREA DE DECLARAÇÃO DE OBJETOS (main code)
# ==========================================
# Instancia a sua TV
minha_tv = ControleRemoto()

while True:
    # 1. Limpa o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # 2. Chama o método que imprime o painel da TV
    minha_tv.mostrar_painel()

    # 3. Pede o input do usuário
    comando = input("On/Off: @ | < CH > | - VOL + | ").strip().lower()

    # 4. Roteador de Comandos
    if comando == '0':
        break  # Sai do programa

    elif comando == '@':
        minha_tv.power()

    elif comando == '+':
        minha_tv.volume_mais()

    elif comando == '-':
        minha_tv.volume_menos()

    elif comando == '>':
        minha_tv.subir_canal()

    elif comando == '<':
        minha_tv.descer_canal()
