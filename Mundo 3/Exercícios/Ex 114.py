# Exercício 114 #
#
# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
#
# Link: pudim.com.br

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 114 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

import requests

try:
    resp = requests.get('https://www.pudim.com.br')
    resp.raise_for_status()

except requests.exceptions.RequestException:
    print("\033[1;31mO site Pudim não está acessível no momento.\033[m")

else:
    print("\033[1;32mConexão estabelecida com sucesso!\033[m")
