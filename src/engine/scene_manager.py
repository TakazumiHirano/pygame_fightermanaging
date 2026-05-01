import pygame


class SceneBase:
    """すべての画面の親となるクラス"""

    def __init__(self):
        self.next_scene = self

    def update(self):
        pass

    def draw(self, screen):
        pass

    def handle_event(self, event):
        pass

    def terminate(self):
        self.next_scene = None
