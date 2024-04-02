import pygame
import math
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("media/backgrounds/background.jpeg")

# Title and icons
pygame.display.set_caption("Space Invaders Remake")
icon = pygame.image.load("media/icons/main_icon.png")
pygame.display.set_icon(icon)

# Main game variables
score = 0
enemies_number = 10
enemies_speed = 0.5

# Player
playerImg = pygame.image.load("media/characters/player.png")
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for i in range(enemies_number):
    enemyImg.append(pygame.image.load("media/characters/enemy.png"))
    enemyX.append(random.randint(1, 730))
    enemyY.append(40)
    enemyX_change.append(enemies_speed)
    enemyY_change.append(40)

def enemy(i, x, y):
    screen.blit(enemyImg[i], (x, y))

# Bullet
bulletImg = pygame.image.load("media/objects/bullet.png")
bulletX = 0
bulletY = 460
bulletY_change = 3
bullet_state = "ready"

def shoot_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 20, y))

# Check if bullet hit an enemy
def enemy_hit(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27 and bullet_state == "fire":
        return True
    return False

# Screen scripts
font = pygame.font.Font("media/fonts/Workbench-Regular.ttf", 32)
textX = 10
textY = 10

def show_score_text(x, y):
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))

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
            elif event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                shoot_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        if event.type == pygame.QUIT:
            running = False

    if bullet_state == "fire":
        shoot_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        if bulletY <= 5:
            bulletY = 460
            bullet_state = "ready"

    if playerX + playerX_change > 2 and playerX + playerX_change < 730:
        playerX += playerX_change
    player(playerX, playerY)

    for i in range(enemies_number):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 2:
            enemyX[i] = 2
            enemyX_change[i] = enemies_speed
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 730:
            enemyX[i] = 730
            enemyX_change[i] = enemies_speed * -1

        collision = enemy_hit(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 460
            bullet_state = "ready"
            score += 1
            # The code below is to regenerate a new enemy when hit
            enemyX[i] = random.randint(1, 730)
            enemyY[i] = 40
            # The code below is to increase the difficulty incresing the enemies speed
            enemies_speed += 0.1
            enemyX_change[i] = enemies_speed
        
        enemy(i, enemyX[i], enemyY[i])
    
    show_score_text(textX, textY)
    pygame.display.update()