print('============ DESAFIO 21 / AULA 08 ============')
print('Reproduzindo audio mp3\n')

import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
