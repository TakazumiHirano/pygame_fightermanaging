import pygame
from src.engine.scene_manager import SceneBase
from config.settings import *


class SettingsScene(SceneBase):
    def __init__(self, previous_scene):
        super().__init__()
        self.previous_scene = previous_scene

    def draw(self, screen):
        screen.fill((50, 50, 50))  # グレー
        font = pygame.font.SysFont("notosanscjp", 40)
        txt = font.render("SETTINGS - CLICK BOTTOM TO BACK", True, COLOR_WHITE)
        screen.blit(txt, (50, SCREEN_HEIGHT // 2))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.pos[1] > SCREEN_HEIGHT // 2:
                self.next_scene = self.previous_scene
