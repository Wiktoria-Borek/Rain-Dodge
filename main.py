import pygame
import time
import random

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Rain Dodge")

BG_ORIGINAL = pygame.image.load("background.jpg")
BG = pygame.transform.smoothscale(BG_ORIGINAL, (WIDTH, HEIGHT))

PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60

def draw_window(player):
    WIN.blit(BG, (0, 0))
    pygame.draw.rect(WIN, (255, 0, 0), player)
    pygame.display.update()

def main():
    global WIDTH, HEIGHT, WIN, BG
    run = True

    player = pygame.Rect(WIDTH//2, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)

    while run:
        draw_window(player)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                BG = pygame.transform.smoothscale(BG_ORIGINAL, (WIDTH, HEIGHT))
    
    pygame.quit()

if __name__ == "__main__":
    main()
