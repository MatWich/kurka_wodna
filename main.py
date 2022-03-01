import pygame
from classes.Mob import Mob
from classes.Window import Window

# screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
# pygame.display.set_caption("Cursor change!")

# cursor = pygame.image.load('img1.png')
# pygame.mouse.set_visible(False)

# mob = Mob(100, 100)


# def update_mouse(cursor_img):
#     coord = pygame.mouse.get_pos()
#     screen.blit(cursor_img, coord)


if __name__ == '__main__':
    # run = True
    #
    # while run:
    #     screen.fill((0, 0, 0))
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             run = False
    #     mob.draw(screen)
    #     update_mouse(cursor)
    #     pygame.display.update()
    win = Window()
    win.mainloop()
