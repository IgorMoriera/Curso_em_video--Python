print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 078 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

valores = list()
rep = list()

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a {cont}º posição: ')))

print('-=' *30)
print(f'Você digitou os  valores: {valores}')

print(f'O MAIOR valor digitado foi {max(valores)} nas posições: ', end='')
for p, v in enumerate(valores):
    if v == max(valores):
        print(f'{p}...', end='')

print(f'\nO MENOR valor digitado foi {min(valores)} nas posições: ', end='')
for p, v in enumerate(valores):
    if v == min(valores):
        print(f'{p}...', end='')

