print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 085 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

valores = [[], []]

for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))

    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

valores[0].sort()
valores[1].sort()

print('-=' * 20)
print(f'Os valores PARES digitados foram: {valores[0]}')
print(f'Os valores ÍMPARES digitados foram: {valores[1]}')
