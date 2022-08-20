#Exemplos da aula 9

'''frase = "Curso em vídeo Phyton"

#Imprimindo a frase
print(frase)

#Fatiando a frase
    # Mostrando a 4ª letra
    print(frase [3])

    # Mostrando da 4ª letra até a 12
        # É possível realizar algumas combinações com esse formato abaixo
    print(frase [3:13])
        # Mostrando do início até a 13ª letra
        print(frase [:13])
        # Mostrando da 13ª letra até o final
    print(frase [13:])
    # Mostrando letras pulando com intervalos
        # É possível realizar algumas combinações com esse formato abaixo
    print(frase [3:13:2])

# Testando funcionalidades
    # função ".cont"
        # Conta q quantidade de letras 'o'. Caso tenha alguma letra em maiusculo, phyton não reconhece
        print(frase.count('o'))
        # Transformando letras para maiusculo (.upper) e contando qnt de letras.
        print( frase.upper().contains('o'))

    # Função 'len()'
        # Contando a quantidadede letras e ESPAÇOS em uma frase
        print(len(frase))
        # Utilizando o '.strip' para remover os espaços na contagem da função 'len()'
        print(len(frase.strip()))

    # Substrtuindo palavras - Função '.replace'
    frase = frase.replace('Phyton', 'Android'))
    print(frase)

    # Verificando de a palavra 'x' está na frase
    print('Curso' in frase) # Resposta: True

    # Buscando/Encontrando a posição das palavras
    print(frase.find('Vídeio')) # caso resposta der '-1', significa que nãotem a palavra ou que não reconheceu a escrita
        # Buscando palavras em maiusculo ou minusculo
        print(frase.upper().find('Vídeio'))
        print(frase.lower().find('Vídeio'))

    # Criando lista - Função '.split'
        print(frase.split()) #Resposta da lista: ['Curso', 'em', 'Vídeo', Phyton']

        #mostrando itens da lista acima separadamente
        dividido = frase.split()
        print(dividido [0]) # OBS: Retorna a 1ª posição da minha lista

        #mostrando uma letra de um dos itens da minha lista
        print(dividido [0] [3])'''