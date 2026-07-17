# Exercício 001 #
#
# Melhorando o primeiro exemplo de objeto

# ==========================================
# ÁREA DE DECLARAÇÃO DA CLASSE (O Molde)
# ==========================================
class Gafanhoto:

    # MÉTODO CONSTRUTOR (__init__)
    # dunder method: "double underscore" (underline) antes e depois
    def __init__(self, nome="vazio", idade=0):
        # ATRIBUTOS DE INSTÂNCIA
        # Aqui definimos as características que todo Gafanhoto terá
        self.nome = nome    # Inicia com nome vazio (string)
        self.idade = idade  # Inicia com a idade valendo 0 (inteiro)

    # MÉTODOS DE INSTÂNCIA
    # Aqui definimos os comportamentos/ações
    def aniversario(self):
        # A idade de "si próprio" (self) ganha + 1
        self.idade += 1

    def mensagem(self):
        # Retorna uma formatação de string pegando os atributos de 'si próprio' (self)
        print(f'{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade.')


# ==========================================
# ÁREA DE DECLARAÇÃO DE OBJETOS (O Programa)
# ==========================================

# Instanciando o primeiro objeto (G1)
g1 = Gafanhoto(n="Ana", i=17)
g1.aniversario()
print(g1.mensagem())

# Instanciando o segundo objeto (G2)
g2 = Gafanhoto(n="Mario", i=53)
g2.aniversario()
print(g2.mensagem())

