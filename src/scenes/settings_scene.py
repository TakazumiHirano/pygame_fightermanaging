import pygame
from . import SceneBase
from config.settings import *


class SettingsScene(SceneBase):
    def __init__(self, controller, data_manager):
        # 親クラスの SceneBase に controller を渡して初期化
        super().__init__(controller, data_manager)

    def draw(self, screen):
        screen.fill((50, 50, 50))  # グレー
        font = pygame.font.SysFont("notosanscjp", 40)
        txt = font.render("SETTINGS - CLICK BOTTOM TO BACK", True, COLOR_WHITE)
        screen.blit(txt, (50, SCREEN_HEIGHT // 2))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.pos[1] > SCREEN_HEIGHT // 2:
                # コントローラに「戻って！」とリクエストする
                self.controller.request_back()
