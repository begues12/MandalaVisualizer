import pygame

class Text:
    def __init__(self, text, x, y, font_size=40, color=(255, 255, 255)):
        self.text = text
        self.position = (x, y)
        self.font_size = font_size
        self.color = color
        self.font = pygame.font.SysFont(None, font_size)

    def draw(self, screen):
        # Render the text
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, self.position)