import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("media/backgrounds/background.jpeg")

# Title and icons
pygame.display.set_caption("Space Invaders Remake")
icon = pygame.image.load("media/icons/main_icon.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("media/characters/player.png")
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Enemy
enemyImg = pygame.image.load("media/characters/enemy.png")
enemyX = random.randint(1, 730)
enemyY = 20
enemyX_change = 1
enemyY_change = 20

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Game loop

running = True

while running:
    # Manage the screen before the characters
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            elif event.key == pygame.K_RIGHT:
                playerX_change = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        if event.type == pygame.QUIT:
            running = False

    if playerX + playerX_change > 2 and playerX + playerX_change < 730:
        playerX += playerX_change
    player(playerX, playerY)

    enemyX += enemyX_change
    if enemyX <= 2:
        enemyX = 2
        enemyX_change = 1
        enemyY += enemyY_change
    elif enemyX >= 730:
        enemyX = 730
        enemyX_change = -1
    enemy(enemyX, enemyY)

    pygame.display.update()