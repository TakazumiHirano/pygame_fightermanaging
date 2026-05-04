import pygame
from config.settings import FONT_NAMES


class AssetManager:
    def __init__(self):
        self.fonts = {}

    def get_font(self, size):
        """一度作ったサイズは保存しておき、二度目はそれを返す"""
        if size not in self.fonts:
            self.fonts[size] = pygame.font.SysFont(FONT_NAMES, size)
        return self.fonts[size]
