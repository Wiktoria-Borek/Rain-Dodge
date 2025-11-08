import pygame
import time
import random

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Rain Dodge")

BG_ORIGINAL = pygame.image.load("background.jpg")
BG = pygame.transform.smoothscale(BG_ORIGINAL, (WIDTH, HEIGHT))

def draw_window():
    WIN.blit(BG, (0, 0))
    pygame.display.update()

def main():
    run = True

    while run:
        draw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.VIDEORESIZE:
                global WIDTH, HEIGHT, WIN, BG
                WIDTH, HEIGHT = event.w, event.h
                WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                BG = pygame.transform.smoothscale(BG_ORIGINAL, (WIDTH, HEIGHT))
    
    pygame.quit()

if __name__ == "__main__":
    main()
