import pygame
from ui.Button import Button

class Menu:
    def __init__(self, app, screen):
        self.app = app
        self.screen = screen
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        self.buttons.append(Button("Resume", 100, 100, 250, 50, self.resume_game))
        self.buttons.append(Button("Create Visuals", 100, 160, 250, 50, self.create_visuals))
        self.buttons.append(Button("View Visuals", 100, 220, 250, 50, self.view_visuals))
        # Agrega más botones según sea necesario

    def draw(self):
        for button in self.buttons:
            button.draw(self.screen)

    def handle_events(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def resume_game(self):
        self.app.state = "running"

    def create_visuals(self):
        # Acción para crear una mandala
        pass
    
    def view_visuals(self):
        self.app.state = "view_visuals"
