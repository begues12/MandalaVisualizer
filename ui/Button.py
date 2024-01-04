import pygame

class Button:
    def __init__(self, text, x, y, w, h, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.action = action
        self.color = (100, 100, 100)  # Color del botón

    def draw(self, screen):
        # Dibuja el botón
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.SysFont(None, 40)
        text = font.render(self.text, True, (255, 255, 255))
        screen.blit(text, (self.rect.x + 20, self.rect.y + 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()