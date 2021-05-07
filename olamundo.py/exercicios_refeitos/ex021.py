'''
ex021: Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
'''

import colorise
import pygame

colorise.set_color(fg='lightred')
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Black Magic Woman_Gypsy Queen.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
print('\nBLACK MAGIC WOMAN / GYPSY QUEEN')
pygame.event.wait()
