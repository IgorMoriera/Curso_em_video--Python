# Exercício 106 #
#
# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
#
# Importante: use cores.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 106 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)


def InteractiveHelp():

    from time import sleep

    while True:
        txt_1 = 'SISTEMA DE AJUDA PyHELP'
        print('\033[1;43m', end='')
        print('~' * (len(txt_1) + 4))
        print(f'  {txt_1}')
        print('~' * (len(txt_1) + 4))

        manual = str(input('\033[mFunção ou Bilbioteca > '))

        if manual == 'fim' or manual == 'FIM':
            txt_3 = 'ATÉ LOGO!'
            print('\033[1;41m~' * (len(txt_3) + 4))
            print(f'  {txt_3}')
            print('~' * (len(txt_3) + 4))
            print('\033[m')
            break

        txt_2 = f"SISTEMA DE AJUDA PyHELP '{manual}'"

        print('\033[1;44m~'*(len(txt_2)+4))
        print(f'  {txt_2}')
        print('~'*(len(txt_2)+4))

        sleep(1)

        print('\033[7;40m')
        help(manual)
        print('\033[m')


InteractiveHelp()
