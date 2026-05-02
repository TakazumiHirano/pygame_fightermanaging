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
        font = pygame.font.SysFont("msgothic", 20)
        for i, log in enumerate(self.battle_logs[-5:]):  # 直近5件を表示
            text = font.render(log, True, (255, 255, 255))
            screen.blit(text, (10, 500 + i * 20))

        # マウスの現在座標を取得
        mouse_pos = pygame.mouse.get_pos()

        # マウスが乗っているキャラを探す
        hovered_char = None
        for char in self.allies + self.enemies:
            if char.rect.collidepoint(mouse_pos):
                hovered_char = char
                break
        # マウスがキャラの上にある場合だけステータスを表示
        if hovered_char:
            self.draw_status_tooltip(screen, hovered_char, mouse_pos)

    def draw_status_tooltip(self, screen, char, pos):
        """ステータスを表示する小さな窓を描画"""
        # 窓の設定
        padding = 10
        line_height = 25
        width, height = 180, 130

        # 画面端で窓が切れないように表示位置を調整
        draw_x = pos[0] + 20
        draw_y = pos[1] + 20
        if draw_x + width > SCREEN_WIDTH:
            draw_x = pos[0] - width - 20

        # 背景の描画（半透明の黒）
        overlay = pygame.Surface((width, height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        screen.blit(overlay, (draw_x, draw_y))

        # 枠線の描画
        pygame.draw.rect(screen, (255, 255, 255),
                         (draw_x, draw_y, width, height), 2)

        # テキストの描画
        font = pygame.font.SysFont("msgothic", 18)
        stats_text = [
            f"NAME: {char.name}",
            f"AGI: {char.agi}",   # AGIベースの行動抽選
            f"STR: {char.str}",
            f"VIT: {char.vit}",   # 基礎能力値
            f"LOYALTY: {char.loyalty}"  # 忠誠度
        ]

        for i, text_str in enumerate(stats_text):
            color = (255, 255, 255)
            # 忠誠度が低い場合に色を変えるなどの演出も可能
            if "LOYALTY" in text_str and char.loyalty < 30:
                color = (255, 100, 100)

            text_surf = font.render(text_str, True, color)
            screen.blit(text_surf, (draw_x + padding,
                        draw_y + padding + i * line_height))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.step_battle()
            pass
        if event.type == pygame.KEYDOWN:
            # 名前でリクエストを送る
            self.controller.request_change("settings")
