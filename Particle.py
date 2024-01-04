import json
import pygame
import math
import random
from Console import Console

class Particle:
    def __init__(self, config, screen_size):
        with open(config, 'r') as config_file:
            config_data = json.load(config_file)
        self.shape = config_data.get("shape", "circle")
        self.color = self.get_color(config_data["color"])
        self.size = random.randint(config_data["size_min"], config_data["size_max"])
        self.size_min = config_data["size_min"]
        self.size_max = config_data["size_max"]
        self.velocity_range = config_data["velocity_range"]
        self.screen_width, self.screen_height = screen_size
        self.x = random.randint(0, self.screen_width)
        self.y = random.randint(0, self.screen_height)
        self.velocity = random.uniform(self.velocity_range[0], self.velocity_range[1])
        self.angle = random.uniform(0, 2 * math.pi)
        self.movement_pattern = config_data.get("movement_pattern", "linear")
        self.reacts_to_sound = config_data.get("reacts_to_sound", False)
        self.image = pygame.image.load(config_data["src"]) if "src" in config_data else None

    def get_color(self, color_config):
        if color_config == "random":
            return [random.randint(0, 255) for _ in range(3)]
        else:
            return color_config

    def update(self, volume_level=0):
        self.update_movement()
        if self.reacts_to_sound:
            self.update_size(volume_level)
    
    def update_movement(self):
        if self.movement_pattern == "linear":
            self.move_linear()
        elif self.movement_pattern == "sine":
            self.move_sine()
        elif self.movement_pattern == "cosine":
            self.move_cosine()
        elif self.movement_pattern == "spiral":
            self.move_spiral()
        elif self.movement_pattern == "random":
            self.move_random()
        elif self.movement_pattern == "horizontal_oscillation":
            self.move_horizontal_oscillation()
        elif self.movement_pattern == "vertical_oscillation":
            self.move_vertical_oscillation()
        elif self.movement_pattern == "circular":
            self.move_circular()
        else:
            self.move_linear()

        # Mantener la partícula dentro de la pantalla
        self.x %= self.screen_width
        self.y %= self.screen_height

    def update_size(self, volume_level):
        scale_factor = 1 + volume_level

        new_size = int(self.size * scale_factor)
        self.size = max(self.size_min, min(new_size, self.size_max))

        if self.image:
            self.image = pygame.transform.scale(self.image, (self.size, self.size))



        

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (int(self.x), int(self.y)))
        else:
            if self.shape == "circle":
                pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
            elif self.shape == "square":
                pygame.draw.rect(screen, self.color, (int(self.x), int(self.y), self.size, self.size))
            elif self.shape == "triangle":
                pygame.draw.polygon(screen, self.color, [(self.x, self.y), (self.x + self.size, self.y), (self.x + self.size / 2, self.y + self.size)])
            elif self.shape == "star":
                pygame.draw.polygon(screen, self.color, [(self.x, self.y + self.size), (self.x + self.size / 2, self.y), (self.x + self.size, self.y + self.size), (self.x, self.y + self.size / 3 * 2), (self.x + self.size, self.y + self.size / 3 * 2)])
            elif self.shape == "cross":
                pygame.draw.line(screen, self.color, (self.x, self.y), (self.x + self.size, self.y + self.size))
                pygame.draw.line(screen, self.color, (self.x + self.size, self.y), (self.x, self.y + self.size))
            elif self.shape == "plus":
                pygame.draw.line(screen, self.color, (self.x + self.size / 2, self.y), (self.x + self.size / 2, self.y + self.size))
            elif self.shape == "ring":
                pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, 1)
            elif self.shape == "dot":
                pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 1)
            elif self.shape == "line":
                pygame.draw.line(screen, self.color, (self.x, self.y), (self.x + self.size, self.y))
            elif self.shape == "rectangle":
                pygame.draw.rect(screen, self.color, (int(self.x), int(self.y), self.size * 2, self.size))
            elif self.shape == "ellipse":
                pygame.draw.ellipse(screen, self.color, (int(self.x), int(self.y), self.size * 2, self.size))
            elif self.shape == "arc":
                pygame.draw.arc(screen, self.color, (int(self.x), int(self.y), self.size * 2, self.size), 0, math.pi / 2)
            elif self.shape == "cloud":
                pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
                pygame.draw.circle(screen, self.color, (int(self.x + self.size / 2), int(self.y)), self.size)
                pygame.draw.circle(screen, self.color, (int(self.x + self.size), int(self.y)), self.size)
                pygame.draw.circle(screen, self.color, (int(self.x + self.size / 4), int(self.y + self.size / 2)), self.size)
                pygame.draw.circle(screen, self.color, (int(self.x + self.size / 4 * 3), int(self.y + self.size / 2)), self.size)
            elif self.shape == "flower":
                pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
                pygame.draw.circle(screen, self.color, (int(self.x + self.size / 2), int(self.y)), self.size)
                pygame.draw.circle(screen, self.color, (int(self.x + self.size), int(self.y)), self.size)
                pygame.draw.circle(screen, self.color, (int(self.x + self.size / 4), int(self.y + self.size / 2)), self.size)
                pygame.draw.circle(screen, self.color, (int(self.x + self.size / 4 * 3), int(self.y + self.size / 2)), self.size)
                pygame.draw.circle(screen, self.color, (int(self.x + self.size / 2), int(self.y + self.size / 4)), self.size)
                pygame.draw.circle(screen, self.color, (int(self.x + self.size / 2), int(self.y + self.size / 4 * 3)), self.size)
            elif self.shape == "heart":
                pygame.draw.polygon(screen, self.color, [(self.x, self.y + self.size / 2), (self.x + self.size / 4, self.y), (self.x + self.size / 2, self.y + self.size / 4), (self.x + self.size / 4 * 3, self.y), (self.x + self.size, self.y + self.size / 2), (self.x + self.size / 2, self.y + self.size), (self.x, self.y + self.size / 2)])
                pygame.draw.circle(screen, self.color, (int(self.x + self.size / 4), int(self.y + self.size / 4)), self.size / 4)
                pygame.draw.circle(screen, self.color, (int(self.x + self.size / 4 * 3), int(self.y + self.size / 4)), self.size / 4)
            else:
                pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
                
    def move_linear(self):
        self.x += math.cos(self.angle) * self.velocity
        self.y += math.sin(self.angle) * self.velocity

    def move_sine(self):
        self.x += self.velocity
        self.y += math.sin(self.time) * 5  # 5 es la amplitud

    def move_cosine(self):
        self.x += self.velocity
        self.y += math.cos(self.time) * 5

    def move_spiral(self):
        self.angle += 0.1
        self.x += math.cos(self.angle) * self.velocity
        self.y += math.sin(self.angle) * self.velocity

    def move_random(self):
        self.x += random.uniform(-1, 1) * self.velocity
        self.y += random.uniform(-1, 1) * self.velocity

    def move_horizontal_oscillation(self):
        self.x += math.sin(self.time) * 5
        self.y += self.velocity

    def move_vertical_oscillation(self):
        self.x += self.velocity
        self.y += math.sin(self.time) * 5
    
    def move_circular(self):
        self.angle += 0.1
        self.x = self.screen_size[0] // 2 + math.cos(self.angle) * 50  # 50 es el radio
        self.y = self.screen_size[1] // 2 + math.sin(self.angle) * 50

