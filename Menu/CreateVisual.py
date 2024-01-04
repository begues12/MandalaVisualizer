import pygame
from ui.Button import Button
from ui.Text import Text
from ui.MandalaThumbnail import MandalaThumbnail
import os
from tkinter import filedialog
import tkinter as tk

class CreateVisual:
    def __init__(self, screen):
        self.screen = screen
        self.menu_width = 200
        self.background_image = None
        self.center_image = None
        self.particle_image = None
        self.bg_button = Button("Background", 10, 40, 180, 40, action=lambda: self.open_file_dialog(self.set_background))
        self.center_button = Button("Center", 10, 100, 180, 40, action=lambda: self.open_file_dialog(self.set_center_image))
        self.particle_button = Button("Particles", 10, 160, 180, 40, action=lambda: self.open_file_dialog(self.set_particle_image))

    def set_background(self, image_path):
        self.background_image = pygame.image.load(image_path)

    def set_center_image(self, image_path):
        self.center_image = pygame.image.load(image_path)

    def set_particle_image(self, image_path):
        self.particle_image = pygame.image.load(image_path)

    def draw(self):
        pygame.draw.rect(self.screen, (50, 50, 50), (0, 0, self.menu_width, self.screen.get_height()))
        self.bg_button.draw(self.screen)
        self.center_button.draw(self.screen)
        self.particle_button.draw(self.screen)

    def handle_event(self, event):
        self.bg_button.handle_event(event)
        self.center_button.handle_event(event)
        self.particle_button.handle_event(event)

    def open_file_dialog(self, callback):
        root = tk.Tk()
        root.withdraw()  # Hides the small tkinter window
        file_path = filedialog.askopenfilename()  # Opens the file dialog
        root.destroy()
        if file_path:
            callback(file_path)
