# VisualManager.py
import os
import threading
from Visual import Visual
from Console import Console
import time
import gc
import pygame
from ui.LoadingBall import LoadingBall
import math

class VisualManager:
    def __init__(self, screen, base_folder_path, screen_size, switch_time=10):
        Console.log("Inicializando VisualManager...")
        self.screen = screen
        self.base_folder_path = base_folder_path
        self.screen_size = screen_size
        self.folder_paths = self.get_folder_paths()
        self.current_visual = None
        self.next_visual = None
        self.visual_loading_thread = None
        self.current_visual_index = 0
        self.switch_time = switch_time  # Tiempo en segundos para cambiar de visual
        self.last_switch_time = time.time()
        self.loading = False
        self.loading_balls = []
        self.init_loading_balls()
        self.start_loading_next_visual()

    def get_folder_paths(self):
        Console.log("Obteniendo rutas de las carpetas de los visuales...")
        return [os.path.join(self.base_folder_path, f)
                for f in os.listdir(self.base_folder_path)
                if os.path.isdir(os.path.join(self.base_folder_path, f))]

    def load_visual(self, folder_path):
        Console.log(f"Cargando visual desde {folder_path}...")
        visual = Visual(self.screen, folder_path, self.screen_size)
        visual.prepare()

        if not self.current_visual:
            self.current_visual = visual
        else:
            self.next_visual = visual

    def start_loading_next_visual(self):
        
        if self.current_visual_index < len(self.folder_paths):
            next_folder_path = self.folder_paths[self.current_visual_index]
            
            self.visual_loading_thread = threading.Thread(target=self.load_visual, args=(next_folder_path,), daemon=True)
            self.visual_loading_thread.start()
            
        self.current_visual_index += 1
        
    def update_and_draw(self, screen, volume_level):
        if self.current_visual:
            self.loading = False
            self.current_visual.update(volume_level)
            self.current_visual.draw(screen)
            
        if self.next_visual and self.should_switch_visual():
            self.switch_to_next_visual()
            
    def should_switch_visual(self):
        # Cambia el visual si ha pasado el tiempo definido
        if time.time() - self.last_switch_time >= self.switch_time:
            self.last_switch_time = time.time()
            return True
        return False


    def switch_to_next_visual(self):
        if self.next_visual:
            # Libera recursos del visual actual
            self.current_visual.cleanup()  # Asegúrate de implementar este método en la clase Visual
            
            # Eliminar explícitamente el visual actual
            del self.current_visual
            
            # Asignar el siguiente visual
            self.current_visual = self.next_visual
            self.next_visual = None

            # Iniciar la carga del próximo visual
            self.start_loading_next_visual()

            # Forzar la recolección de basiv para liberar memoria
            gc.collect()

    def init_loading_balls(self): 
        self.title_font = pygame.font.SysFont("gabriola", 70)
        self.title_text = self.title_font.render("Mandala Visualizer", True, (255, 255, 255))
        self.title_text_rect = self.title_text.get_rect()
        
        center = (self.screen.get_width() // 2, self.screen.get_height() // 2)
        radius = 50
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
        for i in range(6):
            angle = 2 * math.pi * i / 6
            self.loading_balls.append(LoadingBall(center, radius, angle, colors[i]))


    def draw_loading(self):
        self.screen.blit(self.title_text, (self.screen.get_width() // 2 - self.title_text_rect.width // 2, 100))
        for ball in self.loading_balls:
            ball.update()
            ball.draw(self.screen)

