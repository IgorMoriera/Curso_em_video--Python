print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 062 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

a1 = int(input('Digite o 1º termo da P.A: '))
r = int(input('Digite a razão de desejada: '))
an = n = n1  = 0
p = 1
cont = 0
total = 0
m = 10

while m != 0:
    total += m
    while n <= total:
        n += 1
        an = a1 + (n - 1) * r
        print(an, end=' -> ')
    print('PAUSA...')
    m = int(input('Com quantos termos você quer mostrar agora? '))
    cont += m

print('FIM')
print('P.A finzalizada com {} termos mostrados.'.format(cont))
