print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 021 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

import pygame

# Iniciando a biblioteca
pygame.init()

# Carregando a música
pygame.mixer.music.load('ex021.mp3')

# Dando play na música
pygame.mixer.music.play()

# Aguardando a música tocar
pygame.event.wait()


