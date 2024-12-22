import pygame
pygame.init()
X = 500
Y = 500
BLUE = (90, 90, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 247, 15)

cir_x = 150
cir_y = 150

DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			cir_x = cir_x + 20
	
			

	DISPLAY.fill(BLUE)
	pygame.draw.circle(DISPLAY, YELLOW, (cir_x, cir_y), 20)
	pygame.display.flip()