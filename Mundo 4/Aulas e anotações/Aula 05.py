"""

> Os 4 Pilares da POO
        - Abstração: Capacidade de simplificar objetos, removendo detalhes desnecessários.
        - Encapsulamento: Proteção de partes importantes do código contra alterações acidentais.
        - Herança: Trata da hierarquia dos dados (foco da aula atual).
        - Polimorfismo: Capacidade de um mesmo método agir de formas diferentes.

> O que é Herança? (Conceito)
    A Herança é um relacionamento hierárquico entre classes, onde uma classe mais específica (filha) herda atributos
    (características) e métodos (comportamentos) de uma classe mais geral (mãe).
    A Regra do "É UM": A herança é baseada na relação de que o objeto de baixo "é um" objeto do tipo de cima.
    (ex: O Aluno é uma Pessoa).

    >> Terminologias:
        - Classe Superior: Superclasse, Classe Base, Classe Mãe, Ancestral ou Generalização.
        - Classe Inferior: Subclasse, Classe Derivada, Classe Filha, Descendente ou Especialização.
        - Vantagens: Reutilização de código, organização hierárquica, facilidade de manutenção e extensibilidade.

> Exemplo Prático (O Diagrama):
    Em vez de programar os atributos nome, idade e o método fazer_aniversario() três vezes (para Aluno, Professor e
    Funcionário), ele cria uma classe genérica chamada Pessoa.
    As outras três classes são transformadas em subclasses de Pessoa. Assim, o Aluno ganha automaticamente nome e idade
    (da mãe Pessoa), mas pode ter atributos específicos dele, como curso e turma (uma especialização).

> Implementação em Python
    Para fazer a classe Aluno herdar da classe Pessoa no Python, basta colocar o nome da superclasse entre parênteses
    logo após a declaração da classe:

        >> class Aluno(Pessoa):
            - A Função super(): Dentro do método construtor (__init__) da classe filha, é necessário chamar o comando
            super().__init__(...) para repassar os dados comuns (como nome e idade) para a superclasse processar,
            enquanto a filha cuida apenas dos seus atributos específicos (como o curso).

> Boas Práticas: Modularização do Código
    - Separação Simples: Colocar o código principal num arquivo __main__.py e todas as classes juntas em um arquivo
        secundário, utilizando comandos como from classes import Aluno.
    - Separação Profissional: Colocar cada classe em um arquivo Python separado (ex: pessoa.py, aluno.py). Nesse
        cenário, a classe Aluno precisa importar o arquivo de Pessoa antes de realizar a herança.
    - Segurança com o Main: O vídeo também mostra a técnica de envolver a lógica principal em uma função def main():
        e engatilhá-la utilizando a trava de segurança if __name__ == '__main__':.

"""


# Exemplo prático:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazeraniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, curso, turma, nome, idade):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        pass


class Professor(Pessoa):
    def __init__(self, especialidade, nivel):
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        pass


class Funcionario(Pessoa)
    def __init__(self, cargo, setor):
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        pass

