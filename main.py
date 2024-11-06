import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
print("Starting asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")
def main():

    pygame.mixer.init()
    pygame.display.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.joystick.init()
    pygame.joystick.quit()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    shots = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()


    fps = pygame.time.Clock()

    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots, all_sprites)
    updatable.add(player,  asteroid_field)
    drawable.add(player)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for asteroid in asteroids:
            for bullet in shots:
                if pygame.sprite.collide_rect(asteroid, bullet):
                    asteroid.split()
                    bullet.kill()




        time_change = fps.tick(60)
        dt = time_change / 1000
        updatable.update(dt)

        screen.fill((0, 0, 0))

        drawable.draw(screen)





        for sprite in drawable:
            if isinstance(sprite, Asteroid) and player.collides_with(sprite):
                print("Game Over!")
                sys.exit()





        #pygame.sprite.RenderPlain(drawable).draw(screen)
        pygame.display.flip()




if __name__ == "__main__":
    main()

