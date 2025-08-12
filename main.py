import pygame
import asteroid
import asteroidfield
import constants
import player
import shot
import sys
from constants import *

def main():
    pygame.init()
    print("Hello from asteroids-emv!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    shot.Shot.containers = (bullets, updatable, drawable)
    player.Player.containers = (updatable,drawable)
    nzn = player.Player((constants.SCREEN_WIDTH / 2), (constants.SCREEN_HEIGHT / 2))
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable,)
    afield = asteroidfield.AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for aster in asteroids:
            if aster.collides_with(nzn):
                print("Game over!")
                sys.exit()

        screen.fill((0,0,0))

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()

