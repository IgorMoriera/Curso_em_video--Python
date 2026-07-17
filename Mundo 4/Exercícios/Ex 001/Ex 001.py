# Exercício 001 #
#
# Criando o primeiro exemplo de objeto

# ==========================================
# ÁREA DE DECLARAÇÃO DA CLASSE (O Molde)
# ==========================================
class Gafanhoto:

    # MÉTODO CONSTRUTOR (__init__)
    # dunder method: "double underscore" (underline) antes e depois
    def __init__(self):
        # ATRIBUTOS DE INSTÂNCIA
        # Aqui definimos as características que todo Gafanhoto terá
        self.nome = ''  # Inicia com nome vazio (string)
        self.idade = 0  # Inicia com a idade valendo 0 (inteiro)

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
g1 = Gafanhoto()
# NOTA: Os "()" na frente da classe servem para chamar o método
# construtor (__init__), avisando o Python para de fato forjar e construir o objeto na memória.

# Acessando e modificando "Atributos" de g1 (não levam parênteses)
g1.nome = 'Maria'
g1.idade = 17

# Chamando "Métodos" do g1 (levam parênteses indicando a execução da ação)
g1.aniversario()  # Aumentará a idade de 17 para 18.
g1.mensagem()     # Imprimirá os dados de g1 na tela.

# Instanciando o segundo objeto (G2)
g2 = Gafanhoto()
g2.nome = 'Mauro'
g2.idade = 53

# Como quem chamou foi o g2, o "self" na classe saberá que é pra somar a idade do Mauro, e não da Maria.
g2.aniversario()

# Imprimirá: "Mauro é gafanhoto(a) e tem 54 anos de idade"
g2.mensagem()
