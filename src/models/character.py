import os
import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, char_id, data_manager, side, pos):
        super().__init__()
        # データマネージャーから設定を取得
        params = data_manager.get_character_params(char_id)

        self.name = params.get("name", "Unknown")
        self.agi = params.get("agi", 10)  # AGIを読み出し
        self.str = params.get("str", 10)
        self.vit = params.get("vit", 10)
        self.traits = params.get("traits", [])  # 個性[cite: 1]
        self.loyalty = params.get("loyalty", 50)  # 忠誠度[cite: 1]

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
