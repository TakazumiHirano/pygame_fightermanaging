import pygame


class SceneBase:
    """すべての画面の親となるクラス"""

    def __init__(self, controller, data_manager):
        self.controller = controller
        self.data_manager = data_manager

    def update(self):
        pass

    def draw(self, screen):
        pass

    def handle_event(self, event):
        pass

    def terminate(self):
        pass
