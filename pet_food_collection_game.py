import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()

background_image = pygame.transform.scale(pygame.image.load("pet_bg.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("Times New Roman", FONT_SIZE)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")



# Sprite setup

class Sprite(pygame.sprite.Sprite):
    def __init__(self, img, height, width):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img).convert_alpha(), (height, width))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)


all_sprites = pygame.sprite.Group()

pet = Sprite('pet.png', 60, 80)
pet.rect.x, pet.rect.y = random.randint(0, SCREEN_WIDTH - pet.rect.width), random.randint(0, SCREEN_HEIGHT - pet.rect.height)
all_sprites.add(pet)

food = Sprite('golden_apple.png', 50, 50)
food.rect.x, food.rect.y = random.randint(0, SCREEN_WIDTH - food.rect.width), random.randint(0, SCREEN_HEIGHT - food.rect.height)
all_sprites.add(food)

if pet.rect.colliderect(food.rect):
    while pet.rect.colliderect(food.rect):
        pet.rect.x, pet.rect.y = random.randint(0, SCREEN_WIDTH - pet.rect.width), random.randint(0, SCREEN_HEIGHT - pet.rect.height)
        food.rect.x, food.rect.y = random.randint(0, SCREEN_WIDTH - food.rect.width), random.randint(0, SCREEN_HEIGHT - food.rect.height)


running = True
won = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        pet.move(x_change, y_change)

        if pet.rect.colliderect(food.rect):
            all_sprites.remove(food)
            won = True

    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    if won:
        food_collected_text = font.render("Food Collected!", True, pygame.Color('green'))
        screen.blit(food_collected_text, ((SCREEN_WIDTH - food_collected_text.get_width()) // 2, (SCREEN_HEIGHT - food_collected_text.get_height()) // 2))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()