print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 056 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

sidade = 0
media = 0
maiorIdadeHomen = 0
nomeVelho = 0
contM = 0

for pess in range(1, 5):
    print('----- {}ª Pessoa -----'.format(pess))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).upper().strip()

    sidade += idade
# Definindo o homem mais velho
    if pess == 1 and sexo == 'M':
        maiorIdadeHomen = idade
        nomeVelho = nome

    if sexo == 'M' and idade > maiorIdadeHomen:
           maiorIdadeHomen = idade
           nomeVelho = nome

# Definindo a quantidade de mulheres menores do que 20 anos
    if sexo == 'F' and idade < 20:
        contM += 1

# Média das idades
media = sidade / 4

print('\nA media do gupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdadeHomen, nomeVelho))
print('E temos {} mulheres com menos de 20 anos de idade.'.format(contM))

