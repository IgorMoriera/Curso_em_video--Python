# Exercício 090 #
#
# Faça um programa que leia nome e média de um aluno, guradando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 090 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

pessoa = dict()

pessoa['nome'] = str(input('Nome: '))
pessoa['media'] = float(input(f'Média de {pessoa["nome"]}: '))

print(f'- Nome é igual a {pessoa["nome"]}')
print(f'- A média é igual a {pessoa["media"]}')

if pessoa["media"] >= 7.0:
    print('- Situação é igual a \033[1:32mAPROVADO.\033[m')
elif 5.0 <= pessoa["media"] <= 7.0:
    print('- Situação é igual a \033[1:33mRECUPERÇÃO.\033[m')
else:
    print('- Situação é igual a \033[1:31mREPROVADO.\033[m')
