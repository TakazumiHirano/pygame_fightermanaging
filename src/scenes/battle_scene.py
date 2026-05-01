import pygame
import time
from src.engine.scene_manager import SceneBase
from config.settings import *


class BattleScene(SceneBase):
    def __init__(self):
        super().__init__()
        self.start_time = time.time()
        self.duration = 10

    def update(self):
        elapsed = time.time() - self.start_time
        if elapsed >= self.duration:
            from src.scenes.title_scene import TitleScene
            self.next_scene = TitleScene()

    def draw(self, screen):
        screen.fill((100, 30, 30))  # 赤
        font = pygame.font.SysFont("notosanscjp", 40)

        elapsed = time.time() - self.start_time
        remain = max(0, int(self.duration - elapsed))

        txt = font.render(f"BATTLE! TIME LEFT: {remain}s", True, COLOR_WHITE)
        screen.blit(txt, (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT // 2))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            from src.scenes.settings_scene import SettingsScene
            self.next_scene = SettingsScene(self)
