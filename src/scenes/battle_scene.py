import pygame
import time
from . import SceneBase, Character, BattleEngine
from config.settings import *


class BattleScene(SceneBase):
    def __init__(self, controller, data_manager):
        # 親クラスの SceneBase に controller を渡して初期化
        super().__init__(controller, data_manager)
        self.allies = []
        self.enemies = []
        self.setup_characters()

        # 戦闘エンジンの初期化
        self.engine = BattleEngine(self.allies, self.enemies)
        self.battle_logs = ["戦闘開始！"]

    def setup_characters(self):
        """キャラクターの初期配置[cite: 1]"""
        # self.dm = DataManager()

        # 左側（自陣）に2体配置# 「warrior」というIDを指定して生成
        self.allies.append(
            Character("ch001", self.data_manager, "ally", (200, 200)))
        # 「mage」というIDを指定して生成
        self.allies.append(
            Character("ch002", self.data_manager, "ally", (200, 400)))

        # 右側（敵陣）に2体配置
        self.enemies.append(
            Character("enemy001", self.data_manager, "enemy", (600, 200)))
        self.enemies.append(
            Character("enemy001", self.data_manager, "enemy", (600, 400)))

    def update(self):
        # サンプルとして、一定間隔で自動で行動が進むようにする
        # 本来は「司令フェーズ」などの入力待ちを入れる[cite: 1]
        pass

    def step_battle(self):
        """1アクション進める（ボタンクリック等で呼び出す想定）"""
        actor = self.engine.select_next_actor()
        if actor:
            action_log = self.engine.resolve_action(actor)
            self.battle_logs.append(action_log)
        else:
            self.battle_logs.append("フェーズ終了")

    def draw(self, screen):
        screen.fill((50, 100, 50))  # 戦闘フィールドっぽい色

        # 全キャラを描画
        for char in self.allies + self.enemies:
            char.draw(screen)

        super().draw(screen)  # キャラの描画
        # 簡易ログの表示
        font = pygame.font.SysFont("notosanscjp", 20)
        for i, log in enumerate(self.battle_logs[-5:]):  # 直近5件を表示
            text = font.render(log, True, (255, 255, 255))
            screen.blit(text, (10, 500 + i * 20))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.step_battle()
            pass
        if event.type == pygame.KEYDOWN:
            # 名前でリクエストを送る
            self.controller.request_change("settings")
