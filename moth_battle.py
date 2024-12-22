import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,255,0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moth Battle")

# Game variables
avatar_x, avatar_y = WIDTH // 2, HEIGHT - 50
bullet_x, bullet_y = avatar_x, avatar_y
enemy_x, enemy_y = random.randint(0,WIDTH-20), 0
bullet_speed = 5
avatar_speed = 5
enemy_speed = 2
enemies = []
bullets = []

points = 0
lives = 3
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)

running = True
game_close = False

introduction = True

# Fire rate control
fire_rate = 250  # Adjust this value to change the fire rate (milliseconds)
last_bullet_time = 0

# Enemy spawn rate control
spawn_rate = 500  # Adjust this value to change the spawn rate (milliseconds)
last_spawn_time = 0

# Create Rect objects
avatar = pygame.Rect(avatar_x, avatar_y, 30, 30)


def draw_text(text, font, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


# Game loop
while running == True:
    screen.fill(BLACK)

    # Game Over Loop
    
    while game_close == True:
        screen.fill(WHITE)
        
        # checks if the player wins or not, and prompts them what to do next
        if points >= 100:
            draw_text("You Win!", font, GREEN, WIDTH // 2 - 50, HEIGHT // 2)
            draw_text("Press spacebar to play again.", font, BLACK, WIDTH // 2 - 50, HEIGHT // 2 + 50)
            draw_text("Press escape to quit.", font, BLACK, WIDTH // 2 - 50, HEIGHT // 2 + 100)
        else:
            draw_text("Try Again!", font, RED, WIDTH // 2 - 60, HEIGHT // 2)
            draw_text("Press spacebar to play again.", font, BLACK, WIDTH // 2 - 50, HEIGHT // 2 + 50)
            draw_text("Press escape to quit.", font, BLACK, WIDTH // 2 - 50, HEIGHT // 2 + 100)

        pygame.display.flip()
                
        # code to restart game or exit game
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    introduction = True
                    game_close = False
                    points = 0
                    lives = 3
                    avatar_x, avatar_y = WIDTH // 2, HEIGHT - 50
                    avatar = pygame.Rect(avatar_x, avatar_y, 30, 30)
                if event.key == pygame.K_ESCAPE:
                    game_close = False
                    running = False
    
    # introduction screen
    while introduction == True:
        screen.fill(BLACK)
        
        # displays instructions
        draw_text("Use the arrow keys to move.",font,GREEN,50,100)
        draw_text("Use Space Bar to shoot.",font,GREEN,50,140)
        draw_text("Don't get hit by the enemies.",font,GREEN,50,180)
        draw_text("Press any key to start the game.",font,GREEN,50,220)
        
        pygame.display.flip()
        
        # code to start the game
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                introduction = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and avatar.left > 0:
        avatar.x -= avatar_speed
    if keys[pygame.K_RIGHT] and avatar.right < WIDTH:
        avatar.x += avatar_speed
    if keys[pygame.K_UP] and avatar.top > 0:
        avatar.y -= avatar_speed
    if keys[pygame.K_DOWN] and avatar.bottom < HEIGHT:
        avatar.y += avatar_speed

    current_bullet_time = pygame.time.get_ticks()
    if keys[pygame.K_SPACE] and current_bullet_time - last_bullet_time > fire_rate:
        # Create a bullet when the space key is pressed based on fire rate
        new_bullet = pygame.Rect(avatar.x + 10, avatar.y, 10, 10)
        bullets.append(new_bullet)
        last_bullet_time = current_bullet_time  # Update the last bullet time

    # Draw the player (avatar)
    pygame.draw.rect(screen, WHITE, avatar)

    # Draw and move the enemies
    current_spawn_time = pygame.time.get_ticks()
    if len(enemies) < 3 and current_spawn_time - last_spawn_time > spawn_rate:
        enemy_x, enemy_y = random.randint(0,WIDTH-20), 0
        new_enemy = pygame.Rect(enemy_x, enemy_y , 30, 30)
        enemies.append(new_enemy)
        last_spawn_time = current_spawn_time
            
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        pygame.draw.rect(screen, RED, enemy)
        if enemy.y > HEIGHT:
            enemies.remove(enemy)

    # Move and draw bullets, and check for collisions
    for bullet in bullets[:]:  # Iterate over a copy of the list
        bullet.y -= bullet_speed
        pygame.draw.rect(screen, WHITE, bullet)
        
        # Collision detection between bullets and enemies
        for enemy in enemies[:]:  # Iterate over a copy of the list
            if bullet.colliderect(enemy):
                points += 1
                enemies.remove(enemy)
                bullets.remove(bullet)
                break  # Exit the inner loop after collision

        if bullet.y < 0:
            bullets.remove(bullet)
    
    # Checks if an enemy hits the player
    for enemy in enemies[:]:
        if enemy.colliderect(avatar):
            lives -= 1
            enemies.remove(enemy)
            break
    
    # game ending conditions
    if lives <= 0 or points>= 1000:
        game_close = True

    # Display points and lives
    font = pygame.font.Font(None, 36)
    text = font.render(f"Points: {points} Lives: {lives}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(80)

pygame.quit()



"""
#  GAME SET UP

# Creates the objects for the game: a moth, a skull, and enemies.
enemy1 = game.spawnObject("storm","center", -1)
enemy2 = game.spawnObject("storm", "center", -1)
enemy3 = game.spawnObject("storm", "center", -1)

skull = game.spawnObject("skull","center", "bottom")
skull.setScale(0.5)

moth = game.spawnObject("moth","center", "bottom")
moth.setControl("wasd")

# Shows the directions to the player and sets up the border.
game.addTextDirections("Defeat the enemies with skulls of fire! Use WASD keys and don't get hit or touch the walls.")
game.setBorders("infinite")

# Creates variables that will be used during the game.
width = 6
mothSpeed = 0.1
skullSpeed = 0.2

points = 0
lives = 3

# Displays the points and lives for the player
game.setDisplay("points", points)
game.setDisplay("life", lives)

# These functions reset objects to new starting locations.
def initAvatar():
    moth.setXY("center", "bottom")

def initEnemy(enemy):
    mothSpeed = mothSpeed + 0.005
    enemy.setXY(game.random(1, 8), 7)

def initSkull():
    skull.setXY(moth.getX(), moth.getY())

# This function moves an enemy one step down the screen.
def enemyStep(enemy):
    enemy.setY(enemy.getY() - mothSpeed)

# This function checks if an enemy has reached the bottom of the game screen. If it has, then its location resets.
def checkEnemy(enemy):
    if enemy.getY() > 0:
        enemyStep(enemy)
    else:
        initEnemy(enemy)

# Builds a wall on the left and right side of the game screen.
for i in range(8):
    game.spawnObject("wall", 0, i)
    game.spawnObject("wall", 9, i)

# GAME LOOP
# The for loop plays 9999 rounds of the game.
# Look at comments inside the loop to find out what happens in each round.
for frame in range(9999):
    game.advanceGame()
    game.setDisplay("points", points)
    
    # Checks the location of each enemy and moves them one step down the screen.
    checkEnemy(enemy1)
    checkEnemy(enemy2)
    checkEnemy(enemy3)
    
    # Moves the skull one step up the game screen. 
    skull.setY(skull.getY() + skullSpeed)
    
    # Checks if the skull hits any enemy.
    # If so, the player gets a point, the enemy resets, and the moth starts moving faster.
    skullHit = skull.hit("storm")
    if skullHit:
        points = points + 1
        thisStorm = skull.findNearest("storm")
        initEnemy(thisStorm) #  respawn immediately
        initSkull()
        mothSpeed = mothSpeed + 0.01 #  every time you defeat an enemy, the moth gets faster
    
    # Moves the skull back to the moth once it moves off the screen.
    if skull.getY() > 7.5:
        initSkull()

    # Checks if the moth has hit one of the enemies.
    # If so, the player loses a life and the moth location is reset.
    crashEnemy = moth.hit("storm")
    if crashEnemy:
        points = points + 1
        lives = lives - 1
        game.setDisplay("life", lives)
        initAvatar()
        # If the player runs out of lives, then the game ends.
        if lives<1:
            game.end("GAME OVER")
    
    # Checks if the moth has hit one of the walls.
    # If so, the game ends.
    crashWall = moth.hit("wall")
    if crashWall:
        game.end("GAME OVER")
        
    # Keeps the moth from moving off the screen
    if moth.getY()>7:
        moth.setY(7)
    elif moth.getY()<0:
        moth.setY(0)
"""