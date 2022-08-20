print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 046 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

from time import sleep

print('#='*18)
print('{:^}'.format('\033[1;7;40m Contagem regressiva para 2021!!! \033[m'))
print('#='*18)

for c in range(10, -1, -1):
    sleep(1)
    print(c)

print('\033[1;32m-=-\033[m' *6)
print('\033[1;7;40m Um feliz 2021!!! \033[m')
print('\033[1;32m-=-' *6)
