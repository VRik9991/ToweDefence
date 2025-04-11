import pygame


class TowersButton:

    def __init__(self, image, price, image_scale, name, tower_menu_callback):
        self.image = pygame.transform.scale(image, image_scale)
        self.image_rect = [1, 1, 90, 90]
        self.tower_menu_callback = tower_menu_callback
        self.name = name
        self.hit_box = []
        self.text = [price, True, "Blue"]
        self.font = pygame.font.Font("fonts/Ubuntu.png", 20)
        self.price_rect = self.font.render("$" + str(self.text[0]), self.text[1], self.text[2]).get_rect()


    def display(self, screen):
        screen.blit(self.image, self.image_rect)
        screen.blit(self.font.render("$" + str(self.text[0]), self.text[1], self.text[2]),
                    (self.image_rect[0] + ((self.image_rect[2] - self.price_rect[2])/2), self.image_rect[1] + self.image_rect[3]))

    def click(self):
        self.tower_menu_callback(self.name)
