import pygame
pygame.init()
pygame.mixer.music.load('ex021music.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()