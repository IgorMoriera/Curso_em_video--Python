# Exercício 119 #
#
# Crie a classe funcionário, onde podemos cadastrar o nome, setor e cargo. Crie também um método que permita ao
# funcionário se apresentar.

# ==========================================
# ÁREA DE DECLARAÇÃO DA CLASSE (O Molde)
# ==========================================
class Funcionario:

    """
    ...
    """

    # MÉTODO CONSTRUTOR (__init__)
    def __init__(self, nome="", setor="", cargo=""):
        self.nome  = nome
        self.setor = setor
        self.cargo = cargo

    # MÉTODOS DE INSTÂNCIA
    def apresentacao(self):
        return f"Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa CAP"


# ==========================================
# ÁREA DE DECLARAÇÃO DE OBJETOS (main code)
# ==========================================
c1 = Funcionario("Maria", "Administração", "Gerente")
print(c1.apresentacao())

c2 = Funcionario("Geovane", "TI", "Programador")
print(c2.apresentacao())

