import pygame

class MandalaThumbnail:
    def __init__(self, name, background, center, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.border_radius = 10
        self.name = name
        self.background = pygame.transform.scale(background, (w, h))

        center_width, center_height = center.get_size()
        scale_factor = 2 / 3
        new_center_width = int(center_width * scale_factor)
        new_center_height = int(center_height * scale_factor)
        # 2/3 of background size
        self.center = pygame.transform.scale(center, (new_center_width, new_center_height))
        self.center_x = x + (w - new_center_width) // 2
        self.center_y = y + (h - new_center_height) // 2

    def draw(self, screen, scroll_y):
        adjusted_rect = self.rect.move(0, scroll_y)
        pygame.draw.rect(screen, (255, 255, 255), adjusted_rect, border_radius=self.border_radius)
        screen.blit(self.background, adjusted_rect)
        screen.blit(self.center, (self.center_x, self.center_y + scroll_y))


    def get_name(self):
        return self.name