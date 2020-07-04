import pygame
import time
import random
import player
import enemy
import button
import projectile

pygame.init()
#pygame.mixer.init()
#pygame.mixer.music.load('music.mp3')
#pygame.mixer.music.play(-1,0,0)

display_width = 800
display_height = 600
screenSize = display_width, display_height

# colors are represented in RGBa(redvalue, bluevalue, greenvalue, opacityvalue)
colors = {'black': (0, 0, 0, 255),
    'white': (255, 255, 255, 255),
    'light_blue': (53, 115, 255, 255),
    'red' : (200, 0, 0, 255),
    'green' : (0, 200, 0, 255),
    'bright_red' : (255, 0, 0, 255),
    'bright_green' : (0, 255, 0, 255),
    'sky_blue' : (184, 251, 255, 255)}

gameDisplay = pygame.display.set_mode(screenSize)
pygame.display.set_caption('Trolls2')

clock = pygame.time.Clock()
playerImg = pygame.image.load('trollMain.png')
enemyImg = pygame.image.load('soldier.png')
missileImg = pygame.image.load('missile.png')
backgroundImg = pygame.image.load('galaxy.png')

def quitGame():
    pygame.quit()
    quit()

def playerScore(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Score: " + str(count), True, colors['white'])
    gameDisplay.blit(text, (0,0))

def message_display(text, size):
    largeText = pygame.font.SysFont("comicsansms", size)
    TextSurf = largeText.render(text, True, colors['black'])
    TextRect = TextSurf.get_rect()
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)

def crash(player1):
    message_display('You were smashed!', 50)
    player1.resetPlayerMovement()
    pygame.event.clear()
    game_intro()

def createEnemies(numberEnemies, enemieslist):
    for i in range(0, numberEnemies):
        enemieslist.append(enemy.enemy(display_width, display_height, enemyImg, 2))
    return enemieslist

def game_intro():
    StartButton = button.button(150, 450, 100, 50, colors['bright_green'], colors['green'], colors['black'], "comicsansms", 20, game_loop, "Start!")
    ExitButton = button.button(550, 450, 100, 50, colors['bright_red'], colors['red'], colors['black'], "comicsansms", 20, quitGame, "Exit")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()          
        gameDisplay.fill(colors['white'])
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf = largeText.render('Trolls2', True, colors['black'])
        TextRect = TextSurf.get_rect()
        TextRect.center = ((display_width / 2), (display_height / 3))
        gameDisplay.blit(TextSurf, TextRect)
        
        StartButton.idle(gameDisplay)
        ExitButton.idle(gameDisplay)
        
        pygame.display.update()
        clock.tick(15)

def game_loop():
    score = 0
    player1 = player.player(screenSize, playerImg)
    enemies = []
    playerProjectiles = []
    numberEnemies = 10
    createEnemies(numberEnemies, enemies)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                playerProjectiles.append(projectile.projectile(player1, missileImg, 4))
            player1.getPlayerMovement(event)

        #gameDisplay.fill(colors['sky_blue'])
        gameDisplay.blit(backgroundImg, (0,0))

        #projectiles loop
        playerProjectilesCopy = playerProjectiles.copy()
        for i in range(len(playerProjectilesCopy)):
            playerProjectilesCopy[i].updateProjectilePosition(gameDisplay)
            if playerProjectilesCopy[i].detectOffScreen(display_width, display_height) == True:
                del playerProjectiles[i]

        #enemies loop
        for i in enemies:
            i.drawEnemy(gameDisplay)
            if i.detectCollision(player1, playerProjectiles, display_width, display_height) == True:
                crash(player1)
            i.updateEnemyPosition(player1, display_width, display_height)

        #player loop
        player1.updatePlayerPosition()
        if player1.detectCollision(display_width, display_height)  == True:
            crash(player1)
        player1.drawPlayer(gameDisplay)

        #draw the score. always draw score last to prevent it from being covered
        for i in enemies:
            score += i.getTimesHit()
        playerScore(score)
        score = 0

        pygame.display.update()
        clock.tick(60)

game_intro()