from base import Base
import pygame
import time
import os
import random
import neat

from bird import Bird
from pipe import Pipe

WIN_WIDTH = 500
WIN_HEIGHT = 800


BG_IMG = pygame.transform.scale2x(
    pygame.image.load(
        os.path.join('img', 'bg.png')
    )
)


def draw_window(window, bird, pipes, base):
    window.blit(BG_IMG, (0, 0))

    for pipe in pipes:
        pipe.draw(window)

    base.draw(window)
    bird.draw(window)
    pygame.display.update()


def main():
    bird = Bird(230, 350)
    base = Base(730)
    pipes = [Pipe(700)]
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # bird.move()
        for pipe in pipes:
            pipe.move()
        base.move()
        draw_window(window, bird, pipes, base)
    pygame.quit()
    quit()


main()
