import pygame.draw
import random
from circleshape import CircleShape

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
        self.radius = radius
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)) * 100
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)

        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius, 2)

        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.rect.center = (self.position.x, self.position.y)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            random_angle = random.uniform(20, 50)
            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)
            new_velocity1 *= 1.2
            new_velocity2 *= 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            self.kill()

            new_asteroid1 = Asteroid(self.position, new_velocity1, new_radius)
            new_asteroid2 = Asteroid(self.position, new_velocity2, new_radius)


            return [new_asteroid1, new_asteroid2]