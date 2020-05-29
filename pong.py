
import pygame, sys
pygame.init()
clock = pygame.time.Clock()
print(clock)
# setting up the screen

screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')
