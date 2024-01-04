from ui.MandalaThumbnail import MandalaThumbnail
import pygame
import os

class ViewVisuals:
    def __init__(self, screen, mandalas_folder):
        self.screen = screen
        self.mandalas_folder = mandalas_folder
        self.scroll_y = 0
        self.thumbnails = []
        self.load_thumbnails()

    def load_thumbnails(self):
        mandalas = os.listdir(self.mandalas_folder)
        x, y = 15, 50  # Starting coordinates
        width, height = 245, 245  # Thumbnail dimensions
        padding_x, padding_y = 15, 50  # Padding between thumbnails

        for mandala in mandalas:
            background_path = os.path.join(self.mandalas_folder, mandala, "background.png")
            center_path = os.path.join(self.mandalas_folder, mandala, "center.png")
            if os.path.exists(background_path) and os.path.exists(center_path):
                background = pygame.image.load(background_path)
                center = pygame.image.load(center_path)
                # Resize images
                background = pygame.transform.scale(background, (width, height))
                center = pygame.transform.scale(center, (width, height))
                
                thumbnail = MandalaThumbnail(mandala, background, center, x, y, width, height)
                self.thumbnails.append(thumbnail)

                x += width + padding_x
                if x + width > self.screen.get_width():
                    x = 15
                    y += height + padding_y

    def draw(self):
        
        # Text del Menu
        font = pygame.font.SysFont("Arial", 30)
        text = font.render("Visuals", True, (255, 255, 255))
        
        self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, 10 + self.scroll_y))
        
        for thumbnail in self.thumbnails:
            thumbnail.draw(self.screen, self.scroll_y)
            
            # Down text with the name of the mandala centered
            font = pygame.font.SysFont("Arial", 20)
            text = font.render(thumbnail.get_name(), True, (255, 255, 255))
            self.screen.blit(text, (thumbnail.rect.x + thumbnail.rect.width // 2 - text.get_width() // 2, thumbnail.rect.y + thumbnail.rect.height + self.scroll_y))

    def handle_scroll(self, scroll_amount):

        self.scroll_y += scroll_amount