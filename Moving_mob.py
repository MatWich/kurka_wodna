import pygame

from classes.Mob import Mob


class MovingMob(Mob):
    def __init__(self, win, x, y):
        super().__init__(win, x, y)
        self.vel = 1

    def setup_image(self):
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 255, 0))

    def update(self):
        self.rect.x += self.vel

        if self.rect.x < 0 or self.rect.x > 500:
            self.vel *= -1
