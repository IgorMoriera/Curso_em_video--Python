print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 039 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

a = 1 # Masculino
b = 2 # Feminino

ano = int(input('Digite seu ano de nascimento: '))

print('''Qual o seu sexo?
[ 1 ] - Masculino
[ 2 ] - Feminio''')
sexo = int(input('Escolha uma das opções acima: '))


from datetime import date
idade = date.today().year - ano

if sexo == b:
    print('Você não precisa se alistar.')

elif idade < 18 and sexo == a:
    anoo = 18 - idade
    print('\033[1;33mVocê ainda vai se alistar.\033[m Faltam {} anos.'.format(anoo))

elif idade == 18 and sexo == a:
    print('\033[1;31mEstá na hora de você se alistar.\033[m')

elif idade > 18 and sexo == a:
    anooo = idade - 18
    print('\033[1;32mVocê passou {} anos do tempo para se alistar.\033[m'.format(anooo))
