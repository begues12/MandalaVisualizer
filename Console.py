import pygame
import datetime
import sys

class Console:
    @staticmethod
    def log(message):
        # Obtener el tiempo actual
        tick_time = datetime.datetime.now().strftime("%H:%M:%S")

        # Imprime la información con el mensaje
        print(f"[@Console] ({tick_time}) -> {message}")

    def start_loading(self, loading_process_name):
        self.loading_progress = 0
        self.loading_process_name = loading_process_name
        self.update_loading(self.loading_progress)

    def update_loading(self, progress):
        tick_time = datetime.datetime.now().strftime("%H:%M:%S")

        self.loading_progress = progress
        print(f"[@Console] ({tick_time}) [{self.loading_process_name}] -> Loading... {self.loading_progress}%", end="\r")
        sys.stdout.flush()
        
    def update_screen_loading(self, screen):
    #     screen.fill((0, 0, 0))
    #     pygame.draw.rect(screen, (255, 255, 255), (0, 0, screen.get_width() * self.loading_progress / 100, 10))
    #     # And a text to show the percentage
    #    font = pygame.font.SysFont("Arial", 18)
    #     text = font.render(f"{self.loading_progress}%", True, (255, 255, 255))
    #     screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 20))
    #     pygame.display.flip() 
        pass