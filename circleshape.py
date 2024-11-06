import pygame
from pygame.examples.sprite_texture import running


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y



    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        self.position += self.velocity * dt

        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y


    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        print(f"Distance: {distance}, Self radius: {self.radius}, Other radius: {other.radius}")
        if distance <= self.radius + other.radius:
            return True
        else:
            return False