import os
import pygame
from Console import Console

class FrameManager:
    def __init__(self, screen, frames_path):
        self.screen = screen
        self.frames_path = frames_path
        self.frames = []
        self.current_frame_index = 0
        self.console = Console()
        
        self.load_frames()

    def load_frames(self, max_size=(500, 500)):
        filenames = sorted([f for f in os.listdir(self.frames_path) if f.endswith(".png")])
        total_frames = len(filenames)

        self.console.start_loading("Cargando frames: " + self.frames_path)
        
        for index, filename in enumerate(filenames):
            full_path = os.path.join(self.frames_path, filename)
            image = pygame.image.load(full_path)
            
            if image.get_size() != max_size:
                image = pygame.transform.scale(image, max_size)
            
            self.frames.append(image)

            # Actualizar el progreso del loading
            loading_progress = int((index + 1) / total_frames * 100)
            self.console.update_loading(loading_progress)
            self.console.update_screen_loading(self.screen)

    def get_current_frame(self):
        if self.frames:
            return self.frames[self.current_frame_index]
        return None
    
    def update_to_next_frame(self):
        
        if self.frames:
            self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)

            if self.current_frame_index >= len(self.frames):
                self.current_frame_index = 0

    def update_to_previous_frame(self):
        if self.frames:
            self.current_frame_index -= 1
            if self.current_frame_index < 0:
                self.current_frame_index = len(self.frames) - 1

    def get_next_frame(self):
        if self.frames:
            self.update_to_next_frame()
            return self.frames[(self.current_frame_index) % len(self.frames)]
        return None
    
    def get_previous_frame(self):
        if self.frames:
            self.update_to_previous_frame()
            return self.frames[(self.current_frame_index) % len(self.frames)]
        return None

    def draw_current_frame(self, screen):
        current_frame = self.get_current_frame()
        if current_frame:
            screen.blit(current_frame, (0, 0))
