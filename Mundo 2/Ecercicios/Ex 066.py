print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 066 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

cont = soma = 0

while True:
    q = int(input('Digite um número: '))
    print('Digite 999 para parar.')
    if q == 999:
        break
    cont += 1
    soma += q

print(f'''\nVoccê saiu!
Você digitou {cont} e a soma entre esses números deu {soma}.''')
