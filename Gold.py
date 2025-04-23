import pygame
from utils import get_screen_size

class Golda:
    def __init__(self):
        self.screen_size = self.map_size = get_screen_size()
        self.golda_font = pygame.font.Font("fonts/Ubuntu.png", 20)
        self.colour = "Blue"
        self.rect = self.golda_font.render("Gold:", True, self.colour).get_rect()

    def display(self, money: int, screen):
        quantity_money_rect = self.golda_font.render(str(money), True, self.colour).get_rect()
        screen.blit(self.golda_font.render("Gold:", True, self.colour), ((get_screen_size()[0] / 2) - (self.rect[2] + quantity_money_rect[2]) / 2, 1))
        screen.blit(self.golda_font.render(str(money), True, self.colour), ((get_screen_size()[0] / 2) + (self.rect[2] + quantity_money_rect[2]) / 2, 1))