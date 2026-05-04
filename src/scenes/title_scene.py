import pygame
from . import SceneBase
from config.settings import *


class TitleScene(SceneBase):
    def __init__(self, controller, data_manager):
        # 親クラスの SceneBase に controller を渡して初期化
        super().__init__(controller, data_manager)

    def draw(self, screen):
        screen.fill((30, 30, 50))  # 濃い紺
        font = self.controller.asset_manager.get_font(40)

        # 上部（戦闘へ）
        txt_battle = font.render("UPPER: GO TO BATTLE", True, COLOR_WHITE)
        screen.blit(txt_battle, (SCREEN_WIDTH//2 - 150, 150))

        # 下部（設定へ）
        txt_config = font.render("LOWER: GO TO SETTINGS", True, COLOR_WHITE)
        screen.blit(txt_config, (SCREEN_WIDTH//2 - 150, 400))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_y = event.pos[1]
            if mouse_y < SCREEN_HEIGHT // 2:
                # 名前でリクエストを送る
                self.controller.request_change("battle")
            else:  # 画面下部
                self.controller.request_change("settings")
