# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    dt = 0
    
    updatable = pygame.sprite.Group() # Create a group for updatable objects
    drawable = pygame.sprite.Group()  # Create a group for drawable objects
    asteroids = pygame.sprite.Group()  # Create a group for asteroids
    shots = pygame.sprite.Group()  # Create a group for shots
   
    Player.containers = (updatable, drawable)  # Set the containers for the Player class
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Initialize player at the center of the screen
    
    Asteroid.containers = (asteroids, updatable, drawable)  # Set the containers for the Asteroid class
    AsteroidField.containers = (updatable,) # Set the containers for the AsteroidField class
    asteroid_field = AsteroidField()  # Create an instance of the AsteroidField class

    Shot.containers = (shots, updatable, drawable)  # Set the containers for the Shot class

    
    # Main game loop(Infinite loop)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        updatable.update(dt) # Update all updatable objects
        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()  # Exit the game if player collides with an asteroid
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()  # Remove the shot if it collides with an asteroid
                    asteroid.split() # Split the asteroid if it collides with a shot
    
        screen.fill("black")  # Fill the screen with black
        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()  # Update the display
        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time
        
        
    # Print some information to the console
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
if __name__ == "__main__":
    main()