import pygame
from constants import *
import player

def main():
	print("Starting Asteroids!")
	print("Screen width: {}".format(SCREEN_WIDTH))
	print("Screen height: {}".format(SCREEN_HEIGHT))
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	clock = pygame.time.Clock()
	dt = 0

	main_player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	while (True):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		main_player.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60)/1000
		

if __name__ == "__main__":
	main()
