import pygame


class Healthbar:
    def healthbar_run(self, screen, healthbar_user):
        width, height = healthbar_user.image.get_size()
        bar_height = round(height / 5)
        pos_y = round(healthbar_user.rect.y - (height / 5 / 2))
        start_pos = round(healthbar_user.rect.x), pos_y
        end_percent_pos = round(healthbar_user.rect.x + (width / healthbar_user.max_hp) * healthbar_user.current_hp), pos_y
        end_pos = round(healthbar_user.rect.x + width), pos_y
        if healthbar_user.is_alive and healthbar_user.damaged:
            pygame.draw.line(screen, (0, 0, 0), start_pos, end_pos, bar_height)
            pygame.draw.line(screen, (255, 0, 0), start_pos, end_percent_pos, bar_height)
