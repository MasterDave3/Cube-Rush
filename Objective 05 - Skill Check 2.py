import pygame
pygame.init()

X = 400
Y = 400

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 15, 15)
PINK = (255, 15, 179)
PURPLE = (179, 15, 255)
INDIGO = (123, 15, 255)
BLUE = (43, 15, 255)
LIGHT_BLUE = (15, 195, 255)
LIGHT_GREEN = (15, 255, 207)
GREEN = (15, 255, 107)
COLOR = BLACK
 
DISPLAY = pygame.display.set_mode([X, Y])
running = True

pygame.mouse.set_visible(0)
 

while running:
	
	pos = pygame.mouse.get_pos()
	x = pos[0]
	y = pos[1]
	
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		
		if 350 < x:
			COLOR = RED
		elif 300 < x < 350:
			COLOR = PINK
		elif 250 < x < 300:
			COLOR = PURPLE
		elif 200 < x < 250:
			COLOR = INDIGO
		elif 150 < x < 200:
			COLOR = BLUE
		elif 100 < x < 150:
			COLOR = LIGHT_BLUE
		elif 50 < x < 100:
			COLOR = LIGHT_GREEN
		elif 0 < x < 50:
			COLOR = GREEN
		
		
		
	DISPLAY.fill(WHITE)
			

	
	pygame.draw.rect(DISPLAY, COLOR, [x, y, 50, 50])
	
	pygame.display.flip()
	
pygame.quit()