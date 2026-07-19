# Exercício 122 #
#
# Creia a classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao
# fim da leitura.


# Bibliotecas
import time
from rich import print


# ==========================================
# ÁREA DE DECLARAÇÃO DA CLASSE (O Molde)
# ==========================================
class Livro:
    """

    """

    def __init__(self, titulo="", qnt_paginas=0):
        self.titulo = titulo
        self.qnt_paginas = qnt_paginas
        self.pagina_atual = 1

        print(f"""> Você acabou de abrir o livro [blue]"{self.titulo}"[/] que tem [red]{self.qnt_paginas} páginas[/] no total.
    >> Você agora está na [green]Página 1[/]""")
        print(f"\n{"-" * 15}")

    def avancar_paginas(self, qnt=0):
        paginas_lidas_agora = 0

        for i in range(qnt):
            if self.pagina_atual == self.qnt_paginas:

                break
            else:
                self.pagina_atual += 1
                paginas_lidas_agora += 1
                print(f"Pág{self.pagina_atual} >>", end=" ", flush=True)
                time.sleep(0.3)

        print(f"[purple]Você avançou [green]{paginas_lidas_agora}[/] páginas e agora está na Página [yellow]{self.pagina_atual}[/]")

        if self.pagina_atual == self.qnt_paginas:
            print(f"\n[green]Você chegou ao final do livro[/] [blue]'{self.titulo}'[/].")


# ==========================================
# ÁREA DE DECLARAÇÃO DE OBJETOS (main code)
# ==========================================
l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)
