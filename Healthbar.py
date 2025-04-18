import pygame


class Healthbar:
    def healthbar_run(self, screen, healthbar_user):
        width, height = healthbar_user.image.get_size()
        bar_height = round(height / 5)
        pos_y = round(healthbar_user.rect.y - (bar_height / 2))
        start_pos_x = round(healthbar_user.rect.x)
        start_pos = start_pos_x, pos_y
        end_pos_x = round(healthbar_user.rect.x + width)
        healthbar_width = abs(start_pos_x - end_pos_x)
        minuser = healthbar_width / healthbar_user.max_hp
        end_percent_pos_x = round(healthbar_user.rect.x) + abs(minuser * healthbar_user.current_hp)
        end_percent_pos = end_percent_pos_x, pos_y
        if healthbar_user.is_alive:
            pygame.draw.rect(screen, (0, 0, 0), (start_pos_x-1, pos_y-bar_height-1, width+2, bar_height+2))
            pygame.draw.line(screen, (255, 0, 0), start_pos, end_percent_pos, bar_height)
