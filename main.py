import pygame
from constants import *
import player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	print("Starting Asteroids!")
	print("Screen width: {}".format(SCREEN_WIDTH))
	print("Screen height: {}".format(SCREEN_HEIGHT))
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	is_an_asteroid = pygame.sprite.Group()

	player.Player.containers = (updatable, drawable)
	Asteroid.containers = (is_an_asteroid, updatable, drawable)
	AsteroidField.containers = (updatable)

	main_player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	field = AsteroidField()

	while (True):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		updatable.update(dt)

		for asteroid in is_an_asteroid:
			if asteroid.is_colliding(main_player):
				print("Game over!")
				return

		screen.fill("black")
		for drawn in drawable:
			drawn.draw(screen)

		pygame.display.flip()
		
		dt = clock.tick(60)/1000
		

if __name__ == "__main__":
	main()
