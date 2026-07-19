# Exercício 001 #
#
# Melhorando o primeiro exemplo de objeto

# ==========================================
# ÁREA DE DECLARAÇÃO DA CLASSE (O Molde)
# ==========================================
class Gafanhoto:

    """
    Essa classe cria uma Gafanhoto que é uma pessoa que tem um nome e uma idade.
    > Para criar uma nova pessoa, use:
        variavel = Gafanhoto(nome, idade)
    """

    # MÉTODO CONSTRUTOR (__init__)
    # dunder method: "double underscore" (underline) antes e depois
    def __init__(self, nome="", idade=0):
        # ATRIBUTOS DE INSTÂNCIA
        # Aqui definimos as características que todo Gafanhoto terá
        self.nome = nome    # Inicia com nome vazio (string)
        self.idade = idade  # Inicia com a idade valendo 0 (inteiro)

    # MÉTODOS DE INSTÂNCIA
    # Aqui definimos os comportamentos/ações
    def aniversario(self):
        # A idade de "si próprio" (self) ganha + 1
        self.idade += 1

    def __str__(self):
        # Retorna uma formatação de string pegando os atributos de 'si próprio' (self)
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"


# ==========================================
# ÁREA DE DECLARAÇÃO DE OBJETOS (O Programa)
# ==========================================

# Instanciando o primeiro objeto (G1)
g1 = Gafanhoto("Ana", 17)
g1.aniversario()
print(g1)

# Mostra a "documentação" (o manual) de uma classe. Para documentar sua própria classe, basta usar as Docstrings
# (três aspas duplas """) logo abaixo da linha class Nome
print(g1.__doc__)

# Retorna de qual classe aquele objeto se originou.
print(g1.__class__)

# Retorna o "Estado" atual do objeto (todos os seus atributos e valores) formatado como um Dicionário do Python
print(g1.__dict__)  # Método

# Método usado para personalizar como o estado do objeto será exibido. Você pode reescrevê-lo para retornar o estado
# de forma mais elegante do que o __dict__
print(g1.__getstate__())    # Atributo

# Substitui a exibição estranha do endereço de memória de um objeto. Ao reescrever este método com um return, você
# define qual frase em texto o Python deve exibir quando você usar o comando print(objeto)
print(g1.__str__())

# Instanciando o segundo objeto (G2)
g2 = Gafanhoto("Mario", 53)
g2.aniversario()
print(g2)
print(g2.__getstate__())

