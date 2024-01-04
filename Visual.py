import os
from CenterImage import CenterImage
from FrameManager import FrameManager
from ParticleManager import ParticleManager
from Console import Console
class Visual:
    
    def __init__(self, screen, folder_path, screen_size):
        self.screen = screen
        self.folder_path = folder_path
        self.particle_manager = ParticleManager(os.path.join(folder_path, "particles_config.json"), screen_size)
        self.frames = []
        self.frame_manager = FrameManager(self.screen, os.path.join(folder_path, "frames"))
        self.center_image = CenterImage(os.path.join(folder_path, "center.png"), screen_size)
        self.screen_size = screen_size

    def prepare(self):
        self.frames = self.frame_manager.load_frames()
    
    def update(self, volume_level):
        self.volume_level = volume_level
        self.frame_manager.update_to_next_frame()
        self.center_image.update_size(volume_level)
        self.particle_manager.update(volume_level)

    def draw(self, screen):
        current_frame = self.frame_manager.get_current_frame()
        screen.blit(current_frame, current_frame.get_rect(center=(self.screen_size[0] // 2, self.screen_size[1] // 2)))
        
        center_img = self.center_image.get_image()
        screen.blit(center_img, center_img.get_rect(center=(self.screen_size[0] // 2, self.screen_size[1] // 2)))

        self.particle_manager.draw(self.screen)