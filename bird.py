import pygame
import os

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


class Bird:
    IMG = BIRD_IMG
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.velocity = 0
        self.height = 0
        self.image_count = 0
        self.img = self.IMG[0]

    def jump(self):
        self.velocity = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1
        displacement = (self.velocity*self.tick_count) + \
            (1.5 * self.tick_count**2)

        if displacement >= 16:
            displacement = 16

        if displacement < 0:
            displacement -= 2

        self.y = self.y + displacement

        if displacement < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, window):
        self.image_count += 1

        if self.image_count < self.ANIMATION_TIME:
            self.img = self.IMG[0]
        elif self.image_count < self.ANIMATION_TIME * 2:
            self.img = self.IMG[1]
        elif self.image_count < self.ANIMATION_TIME * 3:
            self.img = self.IMG[2]
        elif self.image_count < self.ANIMATION_TIME * 4:
            self.img = self.IMG[1]
        elif self.image_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMG[0]
            self.image_count = 0

        if self.tilt <= -80:
            self.img = self.IMG[1]
            self.image_count = self.ANIMATION_TIME * 2

        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rectangle = rotated_image.get_rect(
            center=self.img.get_rect(
                topleft=(self.x, self.y)
            ).center)

        window.blit(rotated_image, new_rectangle.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
