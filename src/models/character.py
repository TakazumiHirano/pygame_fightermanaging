import os
import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, char_id, data_manager, side, pos):
        super().__init__()
        # データマネージャーから設定を取得
        params = data_manager.get_final_stats(char_id)

        self.name = params["name"]
        self.agi = params["agi"]  # AGIベースの行動抽選
        self.str = params["str"]

        # 画像の読み込み（パスを組み立てる）
        image_name = params.get("image_label", "default.png")
        image_path = os.path.join("assets", "images", image_name)
        self.image = pygame.image.load(image_path).convert_alpha()
        # 画像サイズを調整（例：64x64）
        self.image = pygame.transform.scale(self.image, (64, 64))

        self.rect = self.image.get_rect(center=pos)
        self.side = side  # "ally" or "enemy"

        # 仕様書に基づく基礎能力値の例
        self.hp = 100
        self.agi = 10

    def draw(self, screen):
        screen.blit(self.image, self.rect)
