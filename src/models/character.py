import os
import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, char_id, data_manager, side, pos):
        super().__init__()
        # データマネージャーから設定を取得
        status = data_manager.get_final_stats(char_id)

        # パラメータの取得
        self.name = status["name"]
        self.monmusu_name = status["monmusu_name"]
        self.agi = status["agi"]  # AGIベースの行動抽選
        self.str = status["str"]
        self.vit = status["vit"]
        self.loyalty = status["loyalty"]

        # 画像の読み込み（パスを組み立てる）
        image_name = status.get("image_label", "default.png")
        image_path = os.path.join("assets", "images", image_name)
        self.image = pygame.image.load(image_path).convert_alpha()
        # 画像サイズを調整（例：64x64）
        self.image = pygame.transform.scale(self.image, (64, 64))
        # 位置と範囲の定義
        self.rect = self.image.get_rect(center=pos)

          # "ally" or "enemy"
        self.side = side

        # 仕様書に基づく基礎能力値の例
        self.hp = 100

    def draw(self, screen):
        screen.blit(self.image, self.rect)
