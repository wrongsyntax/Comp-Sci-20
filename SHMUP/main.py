# SHMUP BY UZAIR TARIQ #

import os
import random
import pygame


# Set up asset folder
game_dir = os.path.dirname(__file__)
img_dir = os.path.join(game_dir, "img")
snd_dir = os.path.join(game_dir, "snd")

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

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SHMUP")


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
        self.health = 100
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        # Move player
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP] and self.rect.top > 0:
            self.speedy = -5
        if keystate[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.speedy = 5
        if keystate[pygame.K_LEFT] and self.rect.left > 0:
            self.speedx = -5
        if keystate[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.speedx = 5
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Unhide if hidden
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            BULLETS.add(bullet)
            shoot_sound.play()

    def hide(self):
        # hide the player temporarily
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 1000)


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image_orig = random.choice(meteor_images)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)

        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

        self.rotate()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center


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


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, type):
        pygame.sprite.Sprite.__init__(self)
        self.size = type
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 25

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


font_name = pygame.font.match_font("Arial")


def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


def draw_health_bar(surface, x, y, percent):
    if percent < 0:
        percent = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (percent / 100) * BAR_LENGTH
    outline = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surface, GREEN, fill_rect)
    pygame.draw.rect(surface, WHITE, outline, 2)


def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)


def spawn_mob():
    m = Meteor()
    all_sprites.add(m)
    MOBS.add(m)


def spawn_expl(target, type):
    expl = Explosion(target.rect.center, type)
    all_sprites.add(expl)


def show_go_screen():
    SCREEN.blit(background, background_rect)
    draw_text(SCREEN, "SHMUP!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(SCREEN, "Arrow keys move, Space to fire", 22,
              WIDTH / 2, HEIGHT / 2)
    draw_text(SCREEN, "Press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


# Load game graphics
background = pygame.image.load(os.path.join(img_dir, 'starfield.png'))
background_rect = background.get_rect()
player_img = pygame.image.load(os.path.join(img_dir, "ship.png"))
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)
bullet_img = pygame.image.load(os.path.join(img_dir, "laser.png"))
meteor_images = []
meteor_list = ['meteorGrey_big1.png', 'meteorGrey_big2.png', 'meteorGrey_big3.png', 'meteorGrey_big4.png',
               'meteorGrey_med1.png', 'meteorGrey_med2.png', 'meteorGrey_small1.png', 'meteorGrey_small2.png',
               'meteorGrey_tiny1.png', 'meteorGrey_tiny2.png']
for img in meteor_list:
    meteor_images.append(pygame.image.load(os.path.join(img_dir, img)))

# Load explosion images
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(9):
    filename = "explosion{}.png".format(i)
    img = pygame.image.load(os.path.join(img_dir, filename))
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (65, 65))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    filename = 'playerExplosion{}.png'.format(i)
    img = pygame.image.load(os.path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)

# Load game sounds
shoot_sound = pygame.mixer.Sound(os.path.join(snd_dir, 'pew.wav'))
expl_sounds = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(os.path.join(snd_dir, snd)))
pygame.mixer.music.load(os.path.join(snd_dir, 'bg.ogg'))
pygame.mixer.music.set_volume(0.4)

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

for i in range(8):
    spawn_mob()
score = 0

pygame.mixer.music.play(loops=-1)

# Game loop
game_over = True
running = True

while running:
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        MOBS = pygame.sprite.Group()
        BULLETS = pygame.sprite.Group()
        PLAYER = Spaceship()
        all_sprites.add(PLAYER)
        for i in range(8):
            spawn_mob()
        score = 0
    game_over = False

    # Keep loop running at this speed
    CLOCK.tick(FPS)

    # Process input events
    for event in pygame.event.get():
        # Check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(MOBS, BULLETS, True, True)
    for hit in hits:
        score += 50 - hit.radius
        random.choice(expl_sounds).play()
        spawn_expl(hit, 'lg')
        spawn_mob()

    # Check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(
        PLAYER, MOBS, True, pygame.sprite.collide_circle)
    for hit in hits:
        PLAYER.health -= hit.radius * 2
        spawn_expl(hit, 'sm')
        spawn_mob()
        if PLAYER.health <= 0:
            death_explosion = Explosion(PLAYER.rect.center, 'player')
            all_sprites.add(death_explosion)
            PLAYER.hide()
            PLAYER.lives -= 1
            PLAYER.health = 100

        # if the player died and the explosion has finished playing
        if PLAYER.lives == 0 and not death_explosion.alive():
            game_over = True

    # Draw / render
    SCREEN.fill(BLACK)
    SCREEN.blit(background, background_rect)
    all_sprites.draw(SCREEN)
    draw_text(SCREEN, str(score), 20, WIDTH / 2, 10)
    draw_health_bar(SCREEN, 5, 5, PLAYER.health)
    draw_lives(SCREEN, WIDTH - 100, 5, PLAYER.lives, player_mini_img)

    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
