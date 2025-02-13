# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import *
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shots.containers = (shots, updatable, drawable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        # Inside your game loop
        #print(f"Number of shots: {len(shots)}")
        #print(f"Number of asteroids: {len(asteroids)}")
        for object in asteroids:
            if object.collision(player):
                print("Game Over")
                return
            for shot in shots:
               # print(shot)
                if shot.collision(object):
                   # print("hit asteroid!")
                    object.split()
                    shot.kill()
        for object in drawable:
            object.draw(screen)
        dt = clock.tick(60) / 1000
        pygame.display.flip()
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()