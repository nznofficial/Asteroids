import pygame.draw
import constants
import random
import circleshape
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_var = self.velocity.rotate(random_angle)
            new_neg_var = self.velocity.rotate(-random_angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            new_aster_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_aster_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_aster_1.velocity = new_var*1.2
            new_aster_2.velocity = new_neg_var*1.2

