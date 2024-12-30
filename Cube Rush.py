import pygame # Importing pygame just cuz
import random # Importing random for the lists of ground and clouds and other stuff
import time  # Importing time for the bullet firing thing so far 
pygame.init()

#set game fps
clock = pygame.time.Clock()
FPS = 60

#create game window
X = 900
Y = 400

DISPLAY = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Cube rush")

LIGHTER_RED = (234,93,93)
LIGHT_RED = (229,16,16)
RED = (245,0,0)
LDARK_RED = (187,22,22)
DARK_RED = (149,9,9)
DARKER_RED = (97,10,10)
LIGHT_ORANGE = (229,104,36)
ORANGE = (255,89,0)
DARK_ORANGE = (173,61,0)
VEGAS_GOLD = (196, 180, 84)
WHEAT = (245, 222, 179)
YELLOW_ORANGE = (255, 170, 51)
YELLOW = (255, 255, 0)
YELLOW2 = (240, 255, 15)
NAVYBLUE = (30, 0, 180)
LIGHT_BLUE = (173, 216, 230)
BLUE = (90, 90, 250)
NIGHT_SKY_BLUE = (9,73,134)
CHROMA_KEY_BLUE = (0, 71, 187)
WHITE = (255, 255, 255)
GRAY = (169, 200, 249)
BLACK = (0, 0, 0)
DARK_GREEN = (1, 50, 32)
DARK_GREEN2 = (25,109,9)
GREEN_SCREEN = (0, 177, 64)
GREEN = (0, 255, 0)
LIGHT_GREEN = (31,255,92)
PINK = (174,50,164)
jumpable = True
x=0
tri_x =0
player_y = 270
player_x, playerr_y = X // 2, Y - 50
bullet_x, bullet_y = player_x, player_y
bullet_x, bullet_y = player_x, player_y
enemy_x, enemy_y = random.randint(0,X-20), 0
bullet_speed = 5
player_speed = 5
enemy_speed = 2
enemies = []
bullets = []
ground_list1 = []
ground_list2 = []
ground_list3 = []
ground_list4 = []
ground2_list = []
cloud_list = []
font = pygame.font.Font
last_bullet_time = 0

# Snowflake pixel art
snowflake_art_list = [
    "  *  ",
    " *** ",
    "*****",
    " *** ",
    "  *  "
]
def create_snowflake_surface(snowflake_art_list, color):
    """Creates a Pygame surface from snowflake pixel art."""
    width = len(snowflake_art_list[0])
    height = len(snowflake_art_list)
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    surface.fill((0, 0, 0, 0))  # Transparent background
    for y, row in enumerate(snowflake_art_list):
        for x, char in enumerate(row):
            if char == "*":
                surface.set_at((x, y), color)
    return surface

# Generate snowflakes at a random place
class Snowflake:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.surface = create_snowflake_surface(snowflake_art_list, WHITE)

    def move(self):
        self.y += self.speed
        if self.y > Y:
            self.y = -10  # Reset snow to above the screen
            self.x = random.randint(0, X - len(snowflake_art_list[0]))

    def draw(self, DISPLAY):
        DISPLAY.blit(self.surface, (self.x, self.y))
points = 0
lives = 1
font = pygame.font.SysFont(None, 36)
fire_rate = 250
last_bullet_time = 0
spawn_rate = 500 
last_spawn_time = 0
player = pygame.Rect(30, 340, 50, 50)
# Bullet stuff
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 5)  # Bullet volume
        self.speed = 5

    def move(self):
        self.rect.x += self.speed  # Move bullet sideways to the right

    def draw(self, screen):
        DISPLAY.blit(bullet2, (self.rect))  # Draw the bullet

snowflakes = [Snowflake(random.randint(0, X - 5), random.randint(0, Y), random.randint(1, 3)) for _ in range(50)]
def draw_text(text, font, color, x, y):
    surface = font.render(text, True, color)
    DISPLAY.blit(snow, (x, y))
center = (x+200, 900)



rect = pygame.Rect(30, 340, 50, 50)
rect2 = pygame.Rect(x+200, 200, 50, 50)
rect3 = pygame.Rect(x+300, 200, 50, 50)
rect4 = pygame.Rect(x+400, 200, 50, 50)
obstacle = pygame.Rect(300,200,10,10)
#Defining Game Sprites

apple = pygame.image.load("assets/Apple.png").convert_alpha()
bannana = pygame.image.load("assets/Bannana.png")
ground_with_grass = pygame.image.load("assets/Ground_with_grass.png").convert_alpha()
ground = pygame.image.load("assets/Ground.png").convert_alpha()
water_fall = pygame.image.load("assets/Waterfall.png").convert_alpha()
moon1 = pygame.image.load("assets/moon.png").convert_alpha()
moon2 = pygame.transform.scale(moon1, (150, 150))
sword = pygame.image.load("assets/Sword.png").convert_alpha()
sword2 = pygame.transform.scale(sword, (50, 50))
gun = pygame.image.load("assets/Gun.png").convert_alpha()
milk = pygame.image.load("assets/Milk.png").convert_alpha()
zombie = pygame.image.load("assets/Zombie.png").convert_alpha()
zombie2 = pygame.transform.scale(zombie, (50, 50))
zombie_rect = zombie2.get_rect()
cloud = pygame.image.load("assets/cloud.png").convert_alpha()
cloud2 = pygame.transform.scale(cloud, (150, 100))
bullet = pygame.image.load("assets/bullet.png").convert_alpha()
bullet2 = pygame.transform.scale(bullet, (50, 50))


dinosaur = pygame.image.load("assets/One Armed Dinosaur.png").convert_alpha()
dinosaur2 = pygame.transform.scale(dinosaur, (500, 500))
snow = pygame.image.load("assets/snow.png").convert_alpha()
ground_with_snow = pygame.image.load("assets/ground_with_snow.png").convert_alpha()





running = True  
clock = pygame.time.Clock()
gravity = 0.5
fall_speed = 0

#define game colors variables



# Function to reset the game
def reset_game():
    global points, lives, player, bullets, enemies, last_bullet_time, x, tri_x
    points = 0
    lives = 3
    player = pygame.Rect(30, 340, 50, 50)
    bullets = []
    x = 0
    tri_x = 0
    last_bullet_time = 0
    enemies[:] = [
        pygame.Rect(x + 250, 270, zombie_rect.width, zombie_rect.height),
        pygame.Rect(x + 650, 270, zombie_rect.width, zombie_rect.height),
        pygame.Rect(x + 1050, 270, zombie_rect.width, zombie_rect.height),
        pygame.Rect(x + 1450, 270, zombie_rect.width, zombie_rect.height),
    ]
while running:
    current_time = time.time()  # Getting the current time for bullets
       
    
    tri_x = tri_x -2.25

    x = x - 1
    

    enemies = [
        pygame.Rect(x+250, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+650, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+1050, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+1450, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+1850, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+2250, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+2650, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+3050, 270,zombie_rect.width,zombie_rect.height)
        
    ]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #elif event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_SPACE or jumpable == True:
        #        fall_speed = -10   
        #        jumpable = False 
                
    player.y += fall_speed
    fall_speed += gravity

    

    

    if player.y > 270:
        player_y = 270
        fall_speed = 0
        jumpable = True
    # Update snowflakes
    for snowflake in snowflakes:
        snowflake.move()
    #Draw everything
    DISPLAY.fill(NIGHT_SKY_BLUE)
    





    #runs the game at chosen FPS
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -=5
    if keys[pygame.K_RIGHT]:
        player.x +=5
    if keys[pygame.K_UP] and jumpable == True:
        fall_speed = -10   
        jumpable = False 
    if keys[pygame.K_SPACE]:
#cheat code coming soon    
    # Check if at least 1 second has passed since the last bullet was fired
        if current_time - last_bullet_time >= 1:
            bullet = Bullet(player.x + player.width, player.y + player.height // 8)
            bullets.append(bullet)
            last_bullet_time = current_time  # Updateing the last bullet time

    # Move bullets and check for collisions with enemies
    for bullet in bullets[:]:
        bullet.move()
        if bullet.rect.x > X:
            bullets.remove(bullet)
     # Check collision with each enemy
        for enemy in enemies[:]:
            if bullet.rect.colliderect(enemy):
                enemies.remove(enemy)  # Removes the enemy when it is hit
                bullets.remove(bullet)  # Removes the bullet when it hits the enemy
                break  

    for bullet in bullets:
        bullet.draw(DISPLAY)

    # Move bullets
    for bullet in bullets[:]:
        bullet.move()
        # Remove bullet if it goes off screen
        if bullet.rect.x > X:
            bullets.remove(bullet)
                  
    # Draw and update bullets
    for bullet in bullets:
        bullet.draw(DISPLAY)
    clock.tick(FPS)

    #Drawing Rectangles
    #putting 0 after rect fills the rectangle
    #Drawing circles

    for enemy in enemies:
        DISPLAY.blit(zombie2,enemy.topleft)

        if player.colliderect(enemy):
            lives -= 1
            if lives <= 0:
                DISPLAY.fill(BLACK)
                game_over_text = font.render("Game Over! Restarting, PLease wait....", True, RED)  # Red font for Game Over
                DISPLAY.blit(game_over_text, (X // 3 - 100, Y // 2))
                pygame.display.flip()
                pygame.time.delay(2000)
                reset_game()
            else:
                player.x, player.y = 30, 340
            break
        
    DISPLAY.blit(bullet2, (250, 250))
    #zombie3 = DISPLAY.blit(zombie2, (x+250, 255))
    #zombie3 = DISPLAY.blit(zombie2, (x+450, 255))
    #zombie3 = DISPLAY.blit(zombie2, (x+650, 255))
    #zombie3 = DISPLAY.blit(zombie2, (x+850, 255))
    #zombie3 = DISPLAY.blit(zombie2, (x+1050, 255))
    #zombie3 = DISPLAY.blit(zombie2, (x+1250, 255))
    #zombie3 = DISPLAY.blit(zombie2, (x+1450, 255))
    #zombie3 = DISPLAY.blit(zombie2, (x+1650, 255))
    #zombie3 = DISPLAY.blit(zombie2, (x+1850, 255))
    #zombie3 = DISPLAY.blit(zombie2, (x+2050, 255))
    #zombie3 = DISPLAY.blit(zombie2, (x+2250, 255))
    #zombie3 = DISPLAY.blit(zombie2, (x+2450, 255))
    #zombie3 = DISPLAY.blit(zombie2, (x+2650, 255))
    #zombie3 = DISPLAY.blit(zombie2, (x+2850, 255))
    #zombie3 = DISPLAY.blit(zombie2, (x+3050, 255))
    #zombie3 = DISPLAY.blit(zombie2, (x+3250, 255))
    #zombie3 = DISPLAY.blit(zombie2, (x+2450, 255))



    pygame.draw.rect(DISPLAY, LDARK_RED, player)
    
    gun2 = DISPLAY.blit(gun, (player))



    #Drawing triangles
 
    #Draw Lines


    #Loading sprites
    DISPLAY.blit(milk, (200, 5))
    moon4 = DISPLAY.blit(moon2, (5, 5))
    ground_with_grass2 = DISPLAY.blit(ground_with_snow,(x+150, 350))
    ground_with_grass2_1 = DISPLAY.blit(ground_with_snow,(x+180, 350))
    DISPLAY.blit(ground_with_snow, (150, 390))

    for num in range(0,100,1):
        DISPLAY.blit(ground,(x+(150)+(30*num),370))
        ground_rect = ground.get_rect()
        ground_rect = pygame.Rect(x+(150)+(30*num),370,ground_rect.width, ground_rect.height)
        ground_list1.append(ground_rect)

    for num in range(0,100,1):
        DISPLAY.blit(ground,(x+(150)+(30*num),350))
        ground_rect = ground.get_rect()
        ground_rect = pygame.Rect(x+(150)+(30*num),370,ground_rect.width, ground_rect.height)
        ground_list2.append(ground_rect) 

    for num in range(0,100,1):
        DISPLAY.blit(ground_with_snow,(x+(150)+(30*num),320))
        ground_rect = ground.get_rect()
        ground_rect = pygame.Rect(x+(150)+(30*num),370,ground_rect.width, ground_rect.height)
        ground_list3.append(ground_rect)

    for num in range(0,100,1):
        DISPLAY.blit(ground,(x+(150)+(30*num),390))
        ground_rect = ground.get_rect()
        ground_rect = pygame.Rect(x+(150)+(30*num),370,ground_rect.width, ground_rect.height)
        ground_list4.append(ground_rect)  

    for num in range(0,100,10):
        DISPLAY.blit(cloud2,(x+(195)+(30*num),35))
        ground_rect = ground.get_rect()
        ground_rect = pygame.Rect(x+(150)+(30*num),370,ground_rect.width, ground_rect.height)
        ground_list1.append(ground_rect)

    for num in range(0,100,10):
        DISPLAY.blit(cloud2,(x+(330)+(30*num),50))
        ground_rect = ground.get_rect()
        ground_rect = pygame.Rect(x+(150)+(30*num),370,ground_rect.width, ground_rect.height)
        ground_list1.append(ground_rect)
    ground_with_snow2 = DISPLAY.blit(ground_with_snow,(x+19, 390))
    ground_with_snow2 = DISPLAY.blit(ground_with_snow,(x+110, 390))
    ground_with_snow2 = DISPLAY.blit(ground_with_snow,(x+120, 390))
    ground_with_snow2 = DISPLAY.blit(ground_with_snow,(x+80, 390))
    ground_with_snow2 = DISPLAY.blit(ground_with_snow,(x+60, 390))
    ground_with_snow2 = DISPLAY.blit(ground_with_snow,(x+40, 390))
    ground_with_snow2 = DISPLAY.blit(ground_with_snow,(x+20, 390))
    ground_with_snow2 = DISPLAY.blit(ground_with_snow,(x+10, 390))
    
    for snowflake in snowflakes:
        snowflake.draw(DISPLAY)


    #make player not go through ground:

    if player.bottom > Y:
        player.bottom = Y
        fall_speed = 0
        jumpable = True

    if player.bottom > 320 and player.x > x+150:
        player.bottom = 320
        fall_speed = 0
        jumpable = True
    
    

    #update the screen
    pygame.display.flip()






#exits the game
pygame.quit()   