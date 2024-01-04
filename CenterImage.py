import pygame
from Console import Console

class CenterImage:
    def __init__(self, src, original_size):
        Console.log("Loading center image: " + src + "\n")
        self.src = src
        self.original_image = pygame.image.load(src)
        self.original_size = original_size
        self.current_size = original_size
        Console.log("Center image loaded.")

    def update_size(self, volume_level, max_scale=1.5, max_size=(200, 200)):
        """Ajusta el tamaño de la imagen en función del nivel de volumen."""
        target_scale = 1 + (max_scale - 1) * volume_level
        new_width = int(self.original_size[0] * target_scale)
        new_height = int(self.original_size[1] * target_scale)

        new_width = min(new_width, max_size[0])
        new_height = min(new_height, max_size[1])

        self.current_size = (new_width, new_height)
        self.current_image = pygame.transform.scale(self.original_image, self.current_size)
        
    def get_image(self):
        return self.current_image

    def get_size(self):
        return self.current_size
