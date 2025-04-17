import pygame
import config
import interface

pygame.display.set_caption('Chess')
pygame.init()
pygame.display.init()

screen = pygame.display.set_mode(config.screen_size)
mouse_location = []
running = True
while running:
    clicked = False
    interface.background(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_location.append(pygame.mouse.get_pos())
            clicked = True


    interface.pieces.position(screen,mouse_location,clicked)




    pygame.display.update()
