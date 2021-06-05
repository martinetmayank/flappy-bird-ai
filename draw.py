import pygame
import os

pygame.font.init()

STAT_FONT = pygame.font.SysFont('comicsans', 50)
WIN_WIDTH = 560
BG_IMG = pygame.transform.scale2x(
    pygame.image.load(
        os.path.join('img', 'bg.png')
    )
)


def draw_window(window, birds, pipes, base, score, gen):
    window.blit(BG_IMG, (0, 0))

    for pipe in pipes:
        pipe.draw(window)

    text = STAT_FONT.render(f'Score {score}', 1, (255, 255, 255))
    window.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    text = STAT_FONT.render(f'Gen {gen}', 1, (255, 255, 255))
    window.blit(text, (10, 10))

    base.draw(window)

    for bird in birds:
        bird.draw(window)

    pygame.display.update()
