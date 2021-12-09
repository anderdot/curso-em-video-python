# Desafio 021: Tocar um mp3
from cores import cor
import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Exercicios\ex021.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()
print('Tocando {1}Quando bate aquela saudade{0} do {1}Rubel{0}.'.format(
    cor.reset,
    cor.verde))
pygame.event.wait()
