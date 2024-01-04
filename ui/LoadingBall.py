import pygame
import math

class LoadingBall:
    def __init__(self, center, radius, angle, color):
        self.center = center
        self.radius = radius
        self.angle = angle
        self.color = color

    def update(self):
        # Incrementa el ángulo para girar la bola
        self.angle += 0.05
        if self.angle > 2 * math.pi:
            self.angle -= 2 * math.pi

        # Calcula la nueva posición
        self.x = self.center[0] + math.cos(self.angle) * self.radius
        self.y = self.center[1] + math.sin(self.angle) * self.radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 10)
