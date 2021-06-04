import pygame
import time
import os
import random
import neat


WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMG = [
    pygame.transform.scale2x(
        pygame.image.load(
            os.path.join('img', 'bird1.png')
        )
    ),
    pygame.transform.scale2x(
        pygame.image.load(
            os.path.join('img', 'bird2.png')
        )
    ),
    pygame.transform.scale2x(
        pygame.image.load(
            os.path.join('img', 'bird3.png')
        )
    ),

]


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

PIPE_IMG = pygame.transform.scale2x(
    pygame.image.load(
        os.path.join('img', 'bg.png')
    )
)
