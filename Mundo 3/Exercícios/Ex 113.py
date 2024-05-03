# Exercício 113 #
#
# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
#  de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 113 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)


class Lendonum():

    def leiaInt(self='Digite um valor inteiro: '):

        while True:
            try:
                n = int(input(self))

            except (ValueError, TypeError):
                print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
                continue

            except KeyboardInterrupt:
                print('\n\033[0;31mO usuário preferiu não digitar número algum\033[m.')
                return 0

            else:
                return n

    def leiaFloat(self='Digite um valor Real: '):
        while True:
            try:
                n = float(input(self))

            except (ValueError, TypeError):
                print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
                continue

            except KeyboardInterrupt:
                print('\n\033[0;31mO usuário preferiu não digitar número algum\033[m.')
                return 0

            else:
                return n


num1 = Lendonum.leiaInt()
num2 = Lendonum.leiaFloat()

print('==' * 28)
print(f'-- O valor INTEIRO digitado foi {num1} e o valor REAL {num2}')
print('==' * 28)
print('\033[0;32mVOLTE SEMPRE!\033[m')
