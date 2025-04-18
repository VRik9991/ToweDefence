import pygame
class TowerMenu:
    def __init__(self, buttons, menu_rect):
        self.menu_image = pygame.transform.scale(pygame.image.load('images/Towers_menu.png'),
                                                 (menu_rect[2], menu_rect[3]))
        self.menu_rect = menu_rect
        self.buttons = buttons
        self.chosen_tower = None
        for i in range(len(self.buttons)):
            self.buttons[i].image_rect[1] = self.menu_rect[1]+5
            self.buttons[i].image_rect[0] += ((self.buttons[i].image_rect[3]+10)*i+15)
            self.buttons[i].hit_box = [[self.buttons[i].image_rect[0], self.buttons[i].image_rect[0] + self.buttons[i].image_rect[2]],
                                       [self.buttons[i].image_rect[1], self.buttons[i].image_rect[1] + self.buttons[i].image_rect[3]]]
    def display(self, screen):
        screen.blit(self.menu_image, self.menu_rect)
        for button in self.buttons:
            button.display(screen)