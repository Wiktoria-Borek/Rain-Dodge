import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Rain Dodge")

BG_ORIGINAL = pygame.image.load("background.jpg")
BG = pygame.transform.smoothscale(BG_ORIGINAL, (WIDTH, HEIGHT))

PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60
PLAYER_VEL = 5

FONT = pygame.font.SysFont('comicsans', 30)

def draw_window(player, elapsed_time):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time Survived: {int(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, (255, 0, 0), player)
    pygame.display.update()

def main():
    global WIDTH, HEIGHT, WIN, BG
    run = True

    player = pygame.Rect(WIDTH//2, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    while run:
        clock.tick(60)
        elapsed_time = time.time() - start_time

        draw_window(player, elapsed_time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                BG = pygame.transform.smoothscale(BG_ORIGINAL, (WIDTH, HEIGHT))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL > 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH < WIDTH:
            player.x += PLAYER_VEL
    
    pygame.quit()

if __name__ == "__main__":
    main()
