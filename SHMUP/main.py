# SHMUP BY UZAIR TARIQ #

import os
import pygame
import random


# Set up asset folder
game_dir = os.path.dirname(__file__)
img_dir = os.path.join(game_dir, "img")

# Load game graphics
background = pygame.image.load(os.path.join(img_dir, 'starfield.png'))
background_rect = background.get_rect()
player_img = pygame.image.load(os.path.join(img_dir, "ship.png"))
meteor_img = pygame.image.load(os.path.join(img_dir, "meteor.png"))
bullet_img = pygame.image.load(os.path.join(img_dir, "laser.png"))

WIDTH = 480
HEIGHT = 600
FPS = 60

# Define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (223, 0, 255)

POINTS = 0

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SHMUP")

"""
def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy() 
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
"""


# Spaceship class
class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image = player_img
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.rect = self.image.get_rect()

        # Collision Test
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)

        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        # self.rotate = 0

    def update(self):
        # Move player left and right
        self.speedx = 0
        self.speedy = 0
        # self.rotate = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -5
        if keystate[pygame.K_DOWN]:
            self.speedy = 5
        if keystate[pygame.K_LEFT]:
            # self.rotate = 5
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            # self.rotate = -5
            self.speedx = 5
        # self.rect.y += self.speed
        # self.image = rot_center(self.image, self.rotate)
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Keep player on screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        BULLETS.add(bullet)


# Meteor class for enemies
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image = meteor_img
        self.image = pygame.transform.scale(meteor_img, (65, 50))
        self.rect = self.image.get_rect()

        # Collision Test
        self.radius = 40
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)

        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy

        # Kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


CLOCK = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
MOBS = pygame.sprite.Group()
PLAYER = Spaceship()
BULLETS = pygame.sprite.Group()
all_sprites.add(PLAYER)
for i in range(8):
    m = Meteor()
    all_sprites.add(m)
    MOBS.add(m)

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                PLAYER.shoot()

    # Update
    all_sprites.update()

    # Check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(MOBS, BULLETS, True, True)
    for hit in hits:
        m = Meteor()
        all_sprites.add(m)
        MOBS.add(m)
        POINTS += 1
        print(POINTS)

    # Check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(
        PLAYER, MOBS, False, pygame.sprite.collide_circle)
    if hits:
        running = False

    # Draw / render
    SCREEN.fill(BLACK)
    SCREEN.blit(background, background_rect)
    all_sprites.draw(SCREEN)

    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
