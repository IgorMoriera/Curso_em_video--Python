# Exercício 040 #
#
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 040 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

n1 = float(input('\nDigite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))

media = (n1+n2) / 2

if media < 5.0:
    print('Sua média foi {:.1f}. Você foi \033[1;31mREPROVADO\033[m.'.format(media))

elif 5.0 <= media <= 6.9:
    print('Sua média foi {:.1f}. Você está de \033[1;33mRECUPERAÇÃO\033[m.'.format(media))

elif media >= 7.0:
    print('Sua média foi {:.1f}. Parabéns, você está \033[1;32mAPROVADO\033[m.'.format(media))
