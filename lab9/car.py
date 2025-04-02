import pygame, sys, random, time
from pygame.locals import *


pygame.init()

# fps
FPS = 60
FramePerSec = pygame.time.Clock()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)

# screen setting
SCREEN_WIDTH = 405
SCREEN_HEIGHT = 600

# default setting
SPEED = 5
SCORE = 0
COINS = 0

# font
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# backroung
background = pygame.image.load("AnimatedStreet.png")
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Race")

# enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# class of coin with weight
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.value = random.randint(1, 3)  # coin weight
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

# creation of objects
P1 = Player()
E1 = Enemy()
C1 = Coin()

# sprites group
enemies = pygame.sprite.Group(E1)
coins = pygame.sprite.Group(C1)
all_sprites = pygame.sprite.Group(P1, E1, C1)

# main cycle of game
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # backroung
    DISPLAYSURF.blit(background, (0, 0))

    # signs
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    level = COINS // 5 + 1  # level depends on number of coins
    level_text = font_small.render(f"Level: {level}", True, BLACK)

    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 90, 10))
    DISPLAYSURF.blit(level_text, (SCREEN_WIDTH // 2 - 30, 10))

    # movement of objects
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # hitting the enemy car
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # coin collect
    coin_hit = pygame.sprite.spritecollideany(P1, coins)
    if coin_hit:
        COINS += coin_hit.value  # coin counting
        SPEED += 0.2 * coin_hit.value  # increasement of speed
        coin_hit.kill()

    # creation of new coin
    if len(coins) == 0:
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    pygame.display.update()
    FramePerSec.tick(FPS)

