import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, name, image_path, side, pos):
        super().__init__()
        # 画像の読み込み
        self.image = pygame.image.load(image_path).convert_alpha()
        # 画像サイズを調整（例：64x64）
        self.image = pygame.transform.scale(self.image, (64, 64))
        
        self.rect = self.image.get_rect(center=pos)
        self.name = name
        self.side = side  # "ally" or "enemy"
        
        # 仕様書に基づく基礎能力値の例
        self.hp = 100
        self.agi = 10 

    def draw(self, screen):
        screen.blit(self.image, self.rect)