print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 072 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
       'Onze', 'Doze', 'Treze',  'Quatorze', 'Quinze', 'Desesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

n = int(input('Digite um valor entre 0 e 20: '))

while n > len(num) or n < 0:
    n = int(input('Tente novamente. Digite um valor entre 0 e 20: '))

print(f'Você digitou o numero: {num[n]}.')
