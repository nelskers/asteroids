import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y,  SHOT_RADIUS)
        self.velocity = velocity

        pygame.draw.circle(self.image, (255, 255, 255), (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)