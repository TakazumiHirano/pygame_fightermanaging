import pygame
import sys
from config.settings import *

# 各シーンの制御
from src.engine.scene_manager import SceneController


class Game:
    def __init__(self):
        # Pygameの初期化
        pygame.init()
        # ウィンドウの作成
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        # フレームレート管理用の時計
        self.clock = pygame.time.Clock()

        # コントローラの作成
        # シーンは中の _initialize_scenes が全シーンを準備
        self.controller = SceneController()

        # 最初のシーンを開始
        self.controller.request_change("title")

    def run(self):
        """ゲームループ"""
        while self.controller.current_scene is not None:
            scene = self.controller.current_scene

            # 1. イベント処理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # 現在のシーンにイベントを渡す
                scene.handle_event(event)

            # 2. 更新
            scene.update()

            # 3. 描画
            scene.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
