import pygame

import constants
import player
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
    player.Player.containers = (updatable,drawable)
    player.Player((constants.SCREEN_WIDTH / 2), (constants.SCREEN_HEIGHT / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()

