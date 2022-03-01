import pygame

pygame.init()


class Mob(pygame.sprite.Sprite):
    def __init__(self, win, x, y):
        self.win = win
        pygame.sprite.Sprite.__init__(self, self.win.all_sprites, self.win.ducks)
        self.setup(x, y)

    def setup(self, x, y):
        self.setup_image()
        self.setup_rect(x, y)

    def setup_image(self):
        self.image = pygame.Surface((16, 16))
        self.image.fill((250, 100, 10))

    def setup_rect(self, x, y):
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        pass

    def check_collision(self, bullet_pos: tuple) -> bool:
        x, y = bullet_pos
        if self.rect.left < x < self.rect.right:
            if self.rect.top < y < self.rect.bottom:
                print("that was a hit")
                return True
        return False
