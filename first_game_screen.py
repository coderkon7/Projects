import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

Window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('My first game screen')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()