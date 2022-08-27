# Exercício 021 #
#
# Faça um programa em Python que reproduza o áudio de um arquivo MP3


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 021 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# importando a função 'paygame'
import pygame

# Iniciando a biblioteca
pygame.init()
# Carregando a música
pygame.mixer.music.load('EX021.mp3')
# Dando play na música
pygame.mixer.music.play()

# Por algum motivo, o MEU Pycharm não leu o arquivo mp3.
#  Inserindo os comandos abaixo afim de pausar a música, conseguir rodar o código

# Comando para pausar a música
parar_musica = input('\nTecle algo para parar a música... ')

# Mostrando mensagem na tela
print(' >> Você parou a música! <<')
