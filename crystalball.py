#the best amazing code every wow soo good! right???
import pygame 
import os
from pygame._sdl2 import video as sdl2_video
pygame.init()
pygame.display.set_caption("Crystal Ball")

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
gamerunning = True
dragging = False
#colorzz
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SMOOTHRED = (179, 53, 30)
#textures, balls, stands, etc
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ball_img = pygame.image.load(os.path.join(BASE_DIR, "cball1.png")).convert_alpha()
cball1_img = pygame.transform.scale(ball_img, (300, 300))
ball_rect = cball1_img.get_rect(center=(300, 300))
while gamerunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("ESCAPE KEY PRESSED")
                gamerunning = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            dragging = True
            print("MOUSE BUTTON DOWN")
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragging = False
            print("MOUSE BUTTON UP")
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.fill(BLACK)
    screen.blit(cball1_img, (150, 150))
    pygame.display.update()
    clock.tick(60)