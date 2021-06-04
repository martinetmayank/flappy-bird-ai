import pygame
import time
import os
import random
import neat

from bird import Bird

WIN_WIDTH = 500
WIN_HEIGHT = 800


PIPE_IMG = pygame.transform.scale2x(
    pygame.image.load(
        os.path.join('img', 'pipe.png')
    )
)

BASE_IMG = pygame.transform.scale2x(
    pygame.image.load(
        os.path.join('img', 'base.png')
    )
)

BG_IMG = pygame.transform.scale2x(
    pygame.image.load(
        os.path.join('img', 'bg.png')
    )
)


def draw_window(window, bird):
    window.blit(BG_IMG, (0, 0))
    bird.draw(window)
    pygame.display.update()


def main():
    bird = Bird(200, 200)
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # bird.move()
        draw_window(window,  bird)
    pygame.quit()
    quit()


main()
