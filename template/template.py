# PYGAME TEMPLATE FOR FUTURE PROJECTS #

from pygame.locals import *
import pygame
import sys
import os


# Set up asset folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'resources')

WIDTH = 360
HEIGHT = 480
FPS = 30

# Define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "alien.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

    def update(self):
        self.rect.x += 5


# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME TITLE")
CLOCK = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
PLAYER = Player()
all_sprites.add(PLAYER)

# Game loop
running = True

while running:
    # Keep loop running at this speed
    CLOCK.tick(FPS)

    # Process input events
    for event in pygame.event.get():
        # Check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    SCREEN.fill(BLACK)
    all_sprites.draw(SCREEN)

    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
sys.exit()
