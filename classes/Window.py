import sys

import pygame

from Moving_mob import MovingMob
from classes.CursorManager import CursorManager
from classes.Mob import Mob
from classes.Waepon import Weapon

pygame.init()


class Window:
    def __init__(self):
        self.screen = pygame.display.set_mode((500, 450))
        pygame.display.set_caption("MY TITLE")
        pygame.display.set_icon(pygame.image.load("img1.png"))
        self.run = True
        self.setup()

    def setup(self):
        """ Objects setup """
        self.all_sprites = pygame.sprite.Group()
        self.ducks = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.cursor_manager = CursorManager()
        self.test_sprite = Mob(self, 100, 100)
        self.test_moving_sprite = MovingMob(self, 200, 200)
        self.test_weapon = Weapon(5)

    def mainloop(self):
        while self.run:
            self.dt = self.clock.tick(60) / 1000
            self.controls()
            self.update()
            self.draw()

    def controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.test_weapon.reload()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.onclick_event()

    def update(self):
        self.cursor_manager.update()
        self.all_sprites.update()
        pygame.display.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.cursor_manager.draw(self.screen)
        self.draw_ammo()
        self.print_reload_msg()
        self.all_sprites.draw(self.screen)

    def onclick_event(self):
        if self.test_weapon.empty():
            print("Reload Weapon!!!")
            self.print_reload_msg()
            return
        self.test_weapon.shoot()
        mouse_pos = self.cursor_manager.get_cursor_pos()
        # TODO: handle killing sprites if clicked on it
        for duck in self.ducks:
            if duck.check_collision(mouse_pos):
                duck.kill()

    def draw_ammo(self):
        img = pygame.transform.scale(pygame.image.load("img1.png"), (16, 16))
        for i in range(self.test_weapon.get_ammo()):
            self.screen.blit(img, (
            self.screen.get_width() - img.get_width() - i * img.get_width() - 10, self.screen.get_height() - 32))

    def print_reload_msg(self):
        pygame.font.init()
        font = pygame.font.SysFont("comicsans", 15)
        label = font.render(f"Reload your waepon", 1, (255, 0, 0))
        if self.test_weapon.empty():
            self.screen.blit(label, (self.screen.get_width() / 2 - label.get_width() / 2, self.screen.get_height() / 2))
