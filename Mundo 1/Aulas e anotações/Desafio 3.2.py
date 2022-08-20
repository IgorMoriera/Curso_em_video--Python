print ('===== Desafio 3.2 =====')

# Sempre colocar o tipo de informação antes de iniciar uma operação como: int, str (string), float, bool (True or False)
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))

soma = n1+n2

# print('A soma entre', n1, 'e', n2, 'vale:', soma)

# Utilizar {} para identificar a variável que desejo atribuir
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
