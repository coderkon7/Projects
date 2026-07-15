import pygame

pygame.init()

screenW, screenH = 640, 480

Window = pygame.display.set_mode((screenW, screenH))
Window.fill((255, 255, 255))
pygame.display.set_caption('My first game screen')
welcome_text = pygame.font.Font(None, 36).render('Welcome!', True, pygame.Color('white'), None)
welcome_text_rect = welcome_text.get_rect(center = (screenW // 2, screenH // 2))
rect = pygame.Rect(0, 0, 150, 100)
rect.center = (screenW // 2, screenH // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    rect = pygame.draw.rect(Window, pygame.Color('blue'), rect)
    Window.blit(welcome_text, welcome_text_rect)
    pygame.display.flip()