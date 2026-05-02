import pygame
import time
from . import SceneBase,Character
from config.settings import *

class BattleScene(SceneBase):
    def __init__(self, controller):
        # 親クラスの SceneBase に controller を渡して初期化
        super().__init__(controller)
        self.allies = []
        self.enemies = []
        self.setup_characters()

    def setup_characters(self):
        """キャラクターの初期配置[cite: 1]"""
        # 左側（自陣）に2体配置
        self.allies.append(Character("Hirano", "assets/images/ally.png", "ally", (200, 200)))
        self.allies.append(Character("Yamada", "assets/images/ally.png", "ally", (200, 400)))

        # 右側（敵陣）に2体配置
        self.enemies.append(Character("Enemy_A", "assets/images/enemy.png", "enemy", (600, 200)))
        self.enemies.append(Character("Enemy_B", "assets/images/enemy.png", "enemy", (600, 400)))

    def draw(self, screen):
        screen.fill((50, 100, 50))  # 戦闘フィールドっぽい色
        
        # 全キャラを描画
        for char in self.allies + self.enemies:
            char.draw(screen)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            # 名前でリクエストを送る
            self.controller.request_change("settings")
