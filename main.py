import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Title and icons
pygame.display.set_caption("Space Invaders Remake")
icon = pygame.image.load("media/icons/main_icon.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("media/characters/player.png")
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))

# Game loop

running = True

while running:
    # Manage the screen before the characters
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()