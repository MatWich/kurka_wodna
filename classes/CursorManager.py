import pygame


class CursorManager(pygame.sprite.Sprite):
    SYSTEM_CURSOR_VISIBILITY = False
    AIM_CURSOR_ID = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.current_cursor = self.AIM_CURSOR_ID
        self.AIM_CURSOR_IMG = pygame.image.load('img1.png').convert_alpha()
        self.image = self.AIM_CURSOR_IMG
        self.rect = self.image.get_rect()

        self.position = pygame.mouse.get_pos()
        x, y = pygame.mouse.get_pos()
        self.rect.x = x
        self.rect.y = y

        self.setup()

    def setup(self):
        # pygame.mouse.set_visible(self.SYSTEM_CURSOR_VISIBILITY)
        print("setup")

    def image_switch(self):
        if self.current_cursor == self.AIM_CURSOR_ID:
            self.image = self.AIM_CURSOR_IMG

    def update(self):
        x, y = pygame.mouse.get_pos()
        self.rect.centerx = x
        self.rect.centery = y
        print(x, y)
        self.image_switch()

    def draw(self, screen):
        screen.blit(self.AIM_CURSOR_IMG, self.rect)

    def change_mouse(self, cursor_id):
        if cursor_id is None or cursor_id > 1:
            raise Exception("Unexpected cursor id")
        else:
            self.current_cursor = cursor_id

    def get_cursor_pos(self):
        return self.rect.centerx, self.rect.centery
