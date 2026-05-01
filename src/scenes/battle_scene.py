import pygame
import time
from src.engine.scene_manager import SceneBase
from config.settings import *


class BattleScene(SceneBase):
    def __init__(self, controller):
        # 親クラスの SceneBase に controller を渡して初期化
        super().__init__(controller)
        self.start_time = time.time()
        self.duration = 3

    def update(self):
        elapsed = time.time() - self.start_time
        if elapsed >= self.duration:
            self.controller.request_change("title")

    def draw(self, screen):
        screen.fill((100, 30, 30))  # 赤
        font = pygame.font.SysFont("notosanscjp", 40)

        elapsed = time.time() - self.start_time
        remain = max(0, int(self.duration - elapsed))

        txt = font.render(f"BATTLE! TIME LEFT: {remain}s", True, COLOR_WHITE)
        screen.blit(txt, (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT // 2))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            # 名前でリクエストを送る
            self.controller.request_change("settings")
