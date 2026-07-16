"""

1. O que é uma Classe?
    A Classe é um molde, uma forma, uma estrutura ou um projeto que define as características e os comportamentos de
    algo que será criado. A classe, por si só, não é o item em si, mas sim o seu planejamento.

        >> Exemplo do Biscoito (Bolacha):
            A classe é a forminha de coração que você compra na loja. Você não come a forminha, ela serve exclusivamente
            para garantir que todos os biscoitos tenham a mesma forma padronizada.

        >> Exemplo da Construção Civil:
            A classe é a planta baixa de uma casa desenhada pelo engenheiro ou arquiteto. Você não pode morar na planta,
            mas todo pedreiro deve segui-la para construir uma casa real.

        >> A Estrutura de uma Classe (UML):
            Quando planejamos um sistema, representamos uma classe por meio de um "Diagrama de Classes"
            (conceito de UML), que é um retângulo dividido em 3 partes:

            1. Nome da Classe.
            2. Características (Atributos).
            3. Comportamentos (Métodos).

2. O que são Atributos?
    Os Atributos são as características que todo objeto daquela classe terá. São os "dados" que o objeto guardará.

        Exemplo:
            Numa classe Biscoito de Coração, os atributos podem ser: Tamanho (em cm), Massa (baunilha, chocolate),
            Peso, Cobertura (tem ou não tem?), Cozido (verdadeiro ou falso) e Temperatura.

3. O que são Métodos?
    Os Métodos são as ações que o objeto pode realizar, ou as ações que podem ser feitas com ele.
    Representam o comportamento. Em UML, os métodos costumam ter parênteses () ao final.

        Exemplo:
            Na mesma classe Biscoito de Coração, os métodos poderiam ser: cozinhar(), congelar(), cobrir(),
            confeitar(), comer().

4. O que é Instanciar (ou Instanciamento)?
    Instanciar é o termo técnico para o ato de gerar, forjar ou criar um objeto real a partir de uma classe (molde).

        Exemplo 1:
            Quando você pega a forminha de coração (a classe) e aperta em cima da massa de bolo para fazer o recorte,
            você acabou de instanciar um biscoito.

        Exemplo 2:
            Quando o pedreiro levanta a primeira parede seguindo a planta baixa, ele está instanciando uma casa.

5. O que é um Objeto?
    "Um objeto é a instância de uma classe".
    Um Objeto é a coisa material (concreta) ou abstrata que foi de fato construída a partir de um molde. Ao ser feito
    dessa forma, ele herda exatamente os atributos (características) e métodos (comportamentos) modelados pela classe.

        Exemplos de objetos:
            > Objetos Concretos: Coisas tangíveis (como a caneta, o carro, a casa, o celular, e o próprio biscoito).
            > Objetos Abstratos: Conceitos que não podem ser pegos fisicamente, mas que existem no sistema.
                Consulta médica,
                Processo de venda,
                Transação bancária,
                Erro no Sistema
                    - Tem atributos (código do erro, hora que aconteceu) e métodos (disparar_erro(), corrigir_erro())

6. O que é o Estado de um Objeto?
    O Estado é o conjunto de todos os valores atuais dos atributos de um objeto em um exato momento no tempo.

        Exemplo do Estado:
            Ao pegar um biscoito recém-saído do forno, o estado daquele objeto é: "Massa de Baunilha",
            "Tamanho: 8,2 cm", "Peso: 54,3g", "Cozido: Verdadeiro" e "Temperatura: 55°C".

        Mudança de Estado:
            Se você der uma mordida no biscoito (acionar o método comer()), o peso dele cairá, e a temperatura dele
            diminuirá conforme o tempo passa. Ou seja, o estado do objeto muda através de ações e do tempo, embora os
            seus atributos continuem existindo.

7. Resumo Técnico Definitivo:
    "Um Objeto é uma coisa material ou abstrata, feita a partir de uma Classe, que pode ser descrita por meio de seus
    Atributos (características), Métodos (comportamentos) e de seu Estado atual (os valores exatos que ele carrega
    naquele momento)."

"""