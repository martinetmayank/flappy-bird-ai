from base import Base
import pygame
import time
import os
import random
import neat

from bird import Bird
from pipe import Pipe

pygame.font.init()

WIN_WIDTH = 500
WIN_HEIGHT = 800

STAT_FONT = pygame.font.SysFont('comicsans', 50)

BG_IMG = pygame.transform.scale2x(
    pygame.image.load(
        os.path.join('img', 'bg.png')
    )
)


def draw_window(window, bird, pipes, base, score):
    window.blit(BG_IMG, (0, 0))

    for pipe in pipes:
        pipe.draw(window)

    text = STAT_FONT.render(f'Score {score}', 1, (255, 255, 255))
    window.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    base.draw(window)
    bird.draw(window)

    pygame.display.update()


def main():
    bird = Bird(230, 350)
    base = Base(730)
    pipes = [Pipe(600)]
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    run = True
    clock = pygame.time.Clock()

    score = 0

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # bird.move()
        removed_pipe = list()
        add_pipe = False

        for pipe in pipes:
            if pipe.collide(bird):
                pass
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                removed_pipe.append(pipe)

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True
            pipe.move()

        if add_pipe is True:
            score += 1
            pipes.append(Pipe(600))

        for pipe in removed_pipe:
            pipes.remove(pipe)

        if bird.y + bird.img.get_height() >= 730:
            pass

        base.move()

        draw_window(window, bird, pipes, base, score)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
