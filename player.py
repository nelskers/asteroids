import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED
from shot import Shot
from pygame.math import Vector2

PLAYER_SHOOT_COOLDOWN = 0

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, shots, all_sprites):
        self.timer = PLAYER_SHOOT_COOLDOWN
        pygame.sprite.Sprite.__init__(self)
        CircleShape.__init__(self, x,y, PLAYER_RADIUS)
        self.shot = shots
        self.all_sprites = all_sprites

        self.image = pygame.Surface((PLAYER_RADIUS * 4, PLAYER_RADIUS * 4), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.rotation = 0

    # in the player class
    def triangle(self):
        center = pygame.Vector2(self.radius, self.radius)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        return [a, b, c]


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
           self.shoot()

        self.image.fill((0, 0, 0, 0))
        pygame.draw.polygon(self.image, (255, 255, 255), self.triangle())
        self.rect.center = self.position

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0:
            velocity = Vector2(0,1)
            velocity = velocity.rotate(self.rotation)
            velocity = velocity * PLAYER_SHOT_SPEED


            new_shot = Shot(self.position.x, self.position.y, velocity)
            self.shot.add(new_shot)
            self.all_sprites.add(new_shot)
            self.timer = 0.3

            print("Shots fired")
        else:
            pass


