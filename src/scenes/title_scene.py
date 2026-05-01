import pygame
from src.engine.scene_manager import SceneBase
from config.settings import *


class TitleScene(SceneBase):
    def __init__(self):
        super().__init__()

    def draw(self, screen):
        screen.fill((30, 30, 50))  # 濃い紺
        font = pygame.font.SysFont("notosanscjp", 40)

        # 上部（戦闘へ）
        txt_battle = font.render("UPPER: GO TO BATTLE", True, COLOR_WHITE)
        screen.blit(txt_battle, (SCREEN_WIDTH//2 - 150, 150))

        # 下部（設定へ）
        txt_config = font.render("LOWER: GO TO SETTINGS", True, COLOR_WHITE)
        screen.blit(txt_config, (SCREEN_WIDTH//2 - 150, 400))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_y = event.pos[1]
            if mouse_y < SCREEN_HEIGHT // 2:
                from src.scenes.battle_scene import BattleScene
                self.next_scene = BattleScene()
            else:
                from src.scenes.settings_scene import SettingsScene
                self.next_scene = SettingsScene(self)  # 戻り先として自分を渡す
