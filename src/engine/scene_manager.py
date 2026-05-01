import pygame


class SceneBase:
    """すべての画面の親となるクラス"""

    def __init__(self):
        self.next_scene = None

    def update(self):
        pass

    def draw(self, screen):
        pass

    def handle_event(self, event):
        pass

    def endstep(self):
        self.next_scene = None

    def terminate(self):
        self.next_scene = None
