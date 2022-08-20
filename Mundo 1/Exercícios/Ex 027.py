# Exercício 027 #
#
#


print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 027 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()

print('Seu nome começa com: {}'.format(n[0]))
print('E termina com: {}'.format(n[len(n)-1]))
