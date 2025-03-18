### Mickey Clock ###
import pygame
import sys
import time

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
clock_img = pygame.image.load("mickey.png")
minute_hand = pygame.image.load("right_hand.png")
second_hand = pygame.image.load("left_hand.png")
running = True

while running:
    screen.fill((255, 255, 255))
    current_time = time.localtime()
    minute_angle = -((current_time.tm_min % 60) * 6)
    second_angle = -((current_time.tm_sec % 60) * 6)
    rotated_minute = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second = pygame.transform.rotate(second_hand, second_angle)
    screen.blit(clock_img, (WIDTH//2 - clock_img.get_width()//2, HEIGHT//2 - clock_img.get_height()//2))
    screen.blit(rotated_minute, (WIDTH//2 - rotated_minute.get_width()//2, HEIGHT//2 - rotated_minute.get_height()//2))
    screen.blit(rotated_second, (WIDTH//2 - rotated_second.get_width()//2, HEIGHT//2 - rotated_second.get_height()//2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    pygame.time.Clock().tick(30)
pygame.quit()
sys.exit()
