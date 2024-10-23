import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    dt = 0
    running = True
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while running:
        #Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Calculate dt and update game state
        dt = clock.tick(60) / 1000
        player.update(dt)

        #draw
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    main()