import pygame

# Initializing pygame
pygame.init()

# creating screen
screen = pygame.display.set_mode((800,600))

running = True

#player
playerImage = pygame.image.load('player.png')
playerX = 400
playerY = 360
playerXchange = 0

def player():
    screen.blit(playerImage, (playerX, playerY))

# main game loop
while running:

    # RGB Red, Green, Blue
    screen.fill((26,28,44))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -0.1
            if event.key == pygame.K_RIGHT:
                playerXchange = 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0

    playerX = playerX + playerXchange

    # Showing player
    player()

    #updating display with our color
    pygame.display.update()