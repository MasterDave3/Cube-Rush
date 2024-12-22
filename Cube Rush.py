import pygame 
import random
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
points = 0
lives = 3
font = pygame.font.SysFont(None, 36)
fire_rate = 250
last_bullet_time = 0
spawn_rate = 500 
last_spawn_time = 0
player = pygame.Rect(30, 340, 50, 50)
def draw_text(text, font, color, x, y):
    surface = font.render(text, True, color)
    DISPLAY.blit(surface, (x, y))
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
bullet_x = 50
bullet_y = 0
bullet_state = "loaded"
change_in_y_position_bullet = 4
def shot (bullet_x, bullet_y):
    global bullet_state
    bullet_state = "fired"
    DISPLAY.blit(bullet, (bullet_y, bullet_x))





running = True  
clock = pygame.time.Clock()
gravity = 0.5
fall_speed = 0

#define game colors variables



while running:
       
    
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
        pygame.Rect(x+3050, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+3450, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+3850, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+4250, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+4650, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+5050, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+5450, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+5850, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+6250, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+6650, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+7050, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+7450, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+7850, 270,zombie_rect.width,zombie_rect.height),
        pygame.Rect(x+8250, 270,zombie_rect.width,zombie_rect.height)
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

    DISPLAY.fill(NIGHT_SKY_BLUE)


    if bullet_state == "fired":
        shot(bullet_y, bullet_x)
        bullet_x -= change_in_y_position_bullet


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
        if bullet_state == "loaded":
            bullet_y = player_y
            #shot bullets
            shot(bullet_y, bullet_x)
                  
    #if keys[pygame.K_DOWN]:
    #    player.y +=5
    clock.tick(FPS)

    #Drawing Rectangles
    #putting 0 after rect fills the rectangle
    #Drawing circles

    for enemy in enemies:
        DISPLAY.blit(zombie2,enemy.topleft)

        if player.colliderect(enemy):
            print("you die")
        
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
    ground_with_grass2 = DISPLAY.blit(ground_with_grass,(x+150, 350))
    ground_with_grass2_1 = DISPLAY.blit(ground_with_grass,(x+180, 350))
    DISPLAY.blit(ground_with_grass, (150, 390))

    for num in range(0,1000,1):
        DISPLAY.blit(ground,(x+(150)+(30*num),370))
        ground_rect = ground.get_rect()
        ground_rect = pygame.Rect(x+(150)+(30*num),370,ground_rect.width, ground_rect.height)
        ground_list1.append(ground_rect)

    for num in range(0,500,1):
        DISPLAY.blit(ground,(x+(150)+(30*num),350))
        ground_rect = ground.get_rect()
        ground_rect = pygame.Rect(x+(150)+(30*num),370,ground_rect.width, ground_rect.height)
        ground_list2.append(ground_rect) 

    for num in range(0,500,1):
        DISPLAY.blit(ground_with_grass,(x+(150)+(30*num),320))
        ground_rect = ground.get_rect()
        ground_rect = pygame.Rect(x+(150)+(30*num),370,ground_rect.width, ground_rect.height)
        ground_list3.append(ground_rect)

    for num in range(0,500,1):
        DISPLAY.blit(ground,(x+(150)+(30*num),390))
        ground_rect = ground.get_rect()
        ground_rect = pygame.Rect(x+(150)+(30*num),370,ground_rect.width, ground_rect.height)
        ground_list4.append(ground_rect)  

    for num in range(0,500,10):
        DISPLAY.blit(cloud2,(x+(195)+(30*num),35))
        ground_rect = ground.get_rect()
        ground_rect = pygame.Rect(x+(150)+(30*num),370,ground_rect.width, ground_rect.height)
        ground_list1.append(ground_rect)

    for num in range(0,500,10):
        DISPLAY.blit(cloud2,(x+(330)+(30*num),50))
        ground_rect = ground.get_rect()
        ground_rect = pygame.Rect(x+(150)+(30*num),370,ground_rect.width, ground_rect.height)
        ground_list1.append(ground_rect)


    #make player not go through ground:

    if player.bottom > Y:
        player.bottom = Y
        fall_speed = 0
        jumpable = True

    if player.bottom > 320 and player.x > x+150:
        player.bottom = 320
        fall_speed = 0
        jumpable = True


    #for tile in ground_list1:
    #    if player.colliderect(tile):
    #        player.bottom = tile.top
#
    #for tile in ground_list2:
    #    if player.colliderect(tile):
    #        player.bottom = tile.top
    #
    #for tile in ground_list3:
    #    if player.colliderect(tile):
    #        player.bottom = tile.top
    #
    #for tile in ground_list4:
    #    if player.colliderect(tile):
    #        player.bottom = tile.top

    #ground2 = DISPLAY.blit(ground,(x+150, 370))                
    #ground3 = DISPLAY.blit(ground,(x+180, 370))
    #ground4 = DISPLAY.blit(ground,(x+210, 370))
    #ground5 = DISPLAY.blit(ground,(x+240, 370))
    #ground6 = DISPLAY.blit(ground,(x+270, 370))
    #ground7 = DISPLAY.blit(ground,(x+300, 370))
    #ground8 = DISPLAY.blit(ground,(x+330, 370))
    #ground9 = DISPLAY.blit(ground,(x+360, 370))
    #ground10 = DISPLAY.blit(ground,(x+390, 370))
    #ground11 = DISPLAY.blit(ground,(x+410, 370))
    #ground12 = DISPLAY.blit(ground,(x+440, 370))
    #ground13 = DISPLAY.blit(ground,(x+470,  370))
    #ground14 = DISPLAY.blit(ground,(x+500, 370))
    #ground15 = DISPLAY.blit(ground,(x+530, 370))
    #ground15 = DISPLAY.blit(ground,(x+560, 370))     
    #ground16 = DISPLAY.blit(ground,(x+590, 370))
    #ground17 = DISPLAY.blit(ground,(x+210, 350))
    #ground18 = DISPLAY.blit(ground,(x+240, 350)) 
    #ground19 = DISPLAY.blit(ground,(x+270, 350))
    #ground20 = DISPLAY.blit(ground,(x+300, 350))
    #ground21 = DISPLAY.blit(ground,(x+330, 350))
    #ground22 = DISPLAY.blit(ground,(x+360, 350))
    #ground23 = DISPLAY.blit(ground,(x+390, 350))
    #ground24 = DISPLAY.blit(ground,(x+410, 350))
    #ground25 = DISPLAY.blit(ground,(x+440, 350))
    #ground26 = DISPLAY.blit(ground,(x+470, 350))
    #ground27 = DISPLAY.blit(ground,(x+500, 350))
    #ground28 = DISPLAY.blit(ground,(x+530, 350))
    #ground29 = DISPLAY.blit(ground,(x+560, 350))
    #ground30 = DISPLAY.blit(ground,(x+590, 350))    
    #ground31 = DISPLAY.blit(ground,(x+590, 320))
    #ground32 = DISPLAY.blit(ground,(x+560, 320))  
    #ground33 = DISPLAY.blit(ground,(x+530, 320)) 
    #ground34 = DISPLAY.blit(ground,(x+500, 320)) 
    #ground35 = DISPLAY.blit(ground,(x+470, 320)) 
    #ground36 = DISPLAY.blit(ground,(x+440, 320)) 
    #ground37 = DISPLAY.blit(ground,(x+410, 320)) 
    #ground38 = DISPLAY.blit(ground,(x+380, 320)) 
    #ground39 = DISPLAY.blit(ground,(x+350, 320)) 
    #ground40 = DISPLAY.blit(ground,(x+320, 320)) 
    #ground41 = DISPLAY.blit(ground,(x+290, 320)) 
    #ground42 = DISPLAY.blit(ground,(x+260, 320))
    #ground43 = DISPLAY.blit(ground,(x+230, 320))      
    #ground44 = DISPLAY.blit(ground,(x+210, 320))1000
    ground_with_grass2 = DISPLAY.blit(ground_with_grass,(x+19, 390))
    ground_with_grass2 = DISPLAY.blit(ground_with_grass,(x+110, 390))
    ground_with_grass2 = DISPLAY.blit(ground_with_grass,(x+120, 390))
    ground_with_grass2 = DISPLAY.blit(ground_with_grass,(x+80, 390))
    ground_with_grass2 = DISPLAY.blit(ground_with_grass,(x+60, 390))
    ground_with_grass2 = DISPLAY.blit(ground_with_grass,(x+40, 390))
    ground_with_grass2 = DISPLAY.blit(ground_with_grass,(x+20, 390))
    ground_with_grass2 = DISPLAY.blit(ground_with_grass,(x+10, 390))
    

    #update the screen
    pygame.display.flip()






#exits the game
pygame.quit()   