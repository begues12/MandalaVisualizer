# main.py
import pygame
import sys
from VisualManager import VisualManager
from BassVolumeMonitor import BassVolumeMonitor
from Console import Console
from ui.Menu import Menu
from Menu.ViewVisuals import ViewVisuals
from Menu.CreateVisual import CreateVisual

class MainApp:
    def __init__(self, width, height):
        Console.log("Inicializando la aplicación...")

        pygame.init()
        
        # Inicializa la ventana
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "running"
    
        self.visuals_folder_path = "Visuals"
        
        # Inicializa el VisualManager 
        self.visual_manager = VisualManager(self.screen, self.visuals_folder_path, (width, height))
        Console.log("VisualManager inicializado")

        # Inicializa el monitor de volumen
        self.bass_volume_monitor = BassVolumeMonitor()
        self.bass_volume_monitor.start()
        Console.log("Monitor de volumen iniciado")
        
        # Inicializa las pantallas de menú
        self.menu = Menu(self, self.screen)
        self.view_visuals = ViewVisuals(self.screen, "Visuals")
        self.create_visual = CreateVisual(self.screen)
        
        self.volume_level = 0  # Este valor se actualizará con el nivel real de volumen

    def run(self):
        Console.log("Iniciando la aplicación...")
        while self.running:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.state = "menu" if self.state == "running" else "running"
                elif self.state == "view_visuals" and event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:  # Scroll hacia arriba
                        self.view_visuals.handle_scroll(20)
                    elif event.button == 5:  # Scroll hacia abajo
                        self.view_visuals.handle_scroll(-20)
                
                if self.state == "menu":
                    self.menu.handle_events(event)

            if self.state == "running":
                self.update()
                self.draw()
            elif self.state == "menu":
                self.menu.draw()
            elif self.state == "view_visuals":
                self.view_visuals.draw()
            elif self.state == "create_visual":
                self.create_visual.draw()
                
            pygame.display.flip()
            self.clock.tick(30)

        self.bass_volume_monitor.stop()
        pygame.quit()
        sys.exit()

    def update(self):
        self.volume_level = self.get_volume_level()
        
    def draw(self):
        self.visual_manager.draw_loading()
        self.visual_manager.update_and_draw(self.screen, self.volume_level)

    def start_bass_volume_monitor(self):
        self.bass_volume_monitor.start()

    def get_volume_level(self):
        return self.bass_volume_monitor.get_volume()

if __name__ == "__main__":
    app = MainApp(800, 600)  # Tamaño de la ventana
    app.run()
