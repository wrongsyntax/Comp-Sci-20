import os
import pygame
import sys


# Set up asset folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'resources')

WIDTH = 355
HEIGHT = 355
BOX = 30
MARGIN = 5
FPS = 30

# Define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

grid = []
# Loop for each row
for row in range(10):
    # For each row, create a list that will
    # represent an entire row
    grid.append([])
    # Loop for each column
    for column in range(10):
        # Add a the number zero to the current row
        grid[row].append(0)


class Carrier(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.image.load(os.path.join(img_folder, "alien.png")).convert()
        # self.image.set_colorkey(BLACK)
        # self.rect = self.image.get_rect()
        self.size = 5


class Battleship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 4


class Cruiser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 3


class Submarine(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 3


class Destroyer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 2


# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship")
CLOCK = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
# PLAYER = Player()
# all_sprites.add(PLAYER)

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (BOX + MARGIN)
            row = pos[1] // (BOX + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Grid coordinates: ", row, column)

    # Update
    all_sprites.update()

    # Draw / render
    SCREEN.fill(BLACK)
    all_sprites.draw(SCREEN)
    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(SCREEN,
                             color,
                             [(MARGIN + BOX) * column + MARGIN,
                              (MARGIN + BOX) * row + MARGIN,
                              BOX,
                              BOX])

    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
sys.exit()
