import pygame

pygame.init()

# Note that this project took a while to finish and there was research involved

# BASIC ESSENTIALS
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 400
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CAPTION = pygame.display.set_caption("Game Screen")
FPS = 130
clock = pygame.time.Clock()


# SPRITE CLASS
class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        self.velocity = 5

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
    def moveLeft(self):
        if self.rect.left >= 0: self.rect.x -= self.velocity
        else: self.rect.left = 0  
    def moveRight(self):
        if self.rect.right <= WINDOW_WIDTH: self.rect.x += self.velocity
        else: self.rect.right = WINDOW_WIDTH
    def moveUp(self):
        if self.rect.top >= 0: self.rect.y -= self.velocity
        else: self.rect.top = 0
    def moveDown(self):
        if self.rect.bottom <= WINDOW_HEIGHT: self.rect.y += self.velocity
        else: self.rect.bottom = WINDOW_HEIGHT

    def update(self):
        '''pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if pressed[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if pressed[pygame.K_UP]:
            self.rect.y -= self.velocity
        if pressed[pygame.K_DOWN]:
            self.rect.y += self.velocity'''


        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.moveLeft()
        if pressed[pygame.K_RIGHT]:
            self.moveRight()
        if pressed[pygame.K_UP]:
            self.moveUp()
        if pressed[pygame.K_DOWN]:
            self.moveDown()


        '''if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT'''
    
        




spr1 = Sprite(pygame.Color('blue'), 30, 30)
spr1.rect.x = 100
spr1.rect.y = 100

spr2 = Sprite(pygame.Color('white'), 20, 20)
spr1.rect.x = 100
spr2.rect.y = 100

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add((spr1, spr2))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    

    WINDOW.fill(pygame.Color('black'))
    all_sprites_list.draw(WINDOW)
    spr1.update()
    
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()