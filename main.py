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
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Game loop

running = True

while running:
    # Manage the screen before the characters
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            elif event.key == pygame.K_RIGHT:
                playerX_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        if event.type == pygame.QUIT:
            running = False

    if playerX + playerX_change > 2 and playerX + playerX_change < 730:
        playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()