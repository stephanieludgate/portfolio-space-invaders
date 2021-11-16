import pygame
from pygame import mixer
import math
import random

# initialize the game
pygame.init()

# create the screen (width, height)
screen = pygame.display.set_mode((800,600))

# background image
background = pygame.image.load('images/background.png')

# scores - display
score_value = 0
font_score = pygame.font.Font('freesansbold.ttf',32)
score_padding = 10

def show_score(x,y):
    score = font_score.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))
    
# game over - display
font_game_over = pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
    game_over = font_game_over.render("GAME OVER", True, (255,255,255))
    screen.blit(game_over, (200, 250))

# title and icon (in macOS icon appears in dock)
pygame.display.set_caption("Steph's Space Invaders")
icon = pygame.image.load('images/spaceship.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('images/spaceship.png')
playerX = 368
playerY = 472
playerX_change = 0

# draw player 
def player(x,y):
    screen.blit(playerImg, (x,y))

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range (num_of_enemies):
    enemyImg.append(pygame.image.load('images/alien'+str(i+1)+'.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(0,380))
    enemyX_change.append(2)
    enemyY_change.append(64)

# draw enemy 
def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))
    
# bullet
bulletImg = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

def resetBullet():
    bulletY = 480
    bullet_state = "ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
    
def isCollision(enemyX, enemyY, bulletX, bulletY):
    # using pythagorean theorem backwards to solve for the distance between two points
    distance = math.sqrt( (math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)) )
    if distance < 27:
        return True
    else:
        return False

# game loop
isRunning = True
while isRunning:
    # background image
    screen.blit(background, (0,0))
    
    # events
    for event in pygame.event.get():
        
        # allow user to exit the game
        if event.type == pygame.QUIT:
            isRunning = False
    
        # if keystroke is pressed, check wether it's left, right or spacebar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # bullet sound
                    bullet_sound = mixer.Sound('sounds/laser.wav')
                    bullet_sound.play()
                    # get current x coordinate & store
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    # player movement
    playerX += playerX_change
    
    # player boudaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    # enemy movement
    for i in range(num_of_enemies):
        
        # game over
        if enemyY[i] > 470:
            # if enemy reaches spaceship's x-axis, clear enemies off screen
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        
        enemyX[i] += enemyX_change[i]
        
        # enemy boundaries - once they reach edge of the screen, they shift down y-axis
        if enemyX[i] <= 0:
            
            # increase speed based on score
            if score_value < 20:
                enemyX_change[i] = 2
            elif score_value < 50:
                enemyX_change[i] = 3
            else:
                enemyX_change[i] = 4
                
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            
            # increase speed based on score
            if score_value < 20:
                enemyX_change[i] = -2
            elif score_value < 50:
                enemyX_change[i] = -3
            else:
                enemyX_change[i] = -4
                
            enemyY[i] += enemyY_change[i]
        
        # collision detection
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            # reset bullet
            bulletY = 480
            bullet_state = "ready"
            # increase score
            score_value += 1
            #re-spawn enemy
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(0,380)
        
        enemy(enemyX[i], enemyY[i], i)
    
    # bullet movement
    if bulletY <= 0:
        # this should be a function
        bulletY = 480
        bullet_state = "ready"
    
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
        
    player(playerX,playerY)
    
    show_score(score_padding,score_padding)
    
    # update display continuously
    pygame.display.update()


