import pygame
import sys
from config.settings import *
from src.scenes.title_scene import TitleScene


class Game:
    def __init__(self):
        # Pygameの初期化
        pygame.init()
        # ウィンドウの作成
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        # フレームレート管理用の時計
        self.clock = pygame.time.Clock()
        # 最初のシーンをセット
        self.scene = TitleScene()

    def run(self):
        """ゲームループ"""
        while self.scene is not None:
            # 1. イベント処理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # 現在のシーンにイベントを渡す
                self.scene.handle_event(event)

            # 2. 更新
            self.scene.update()

            # シーンの切り替えチェック
            if self.scene != self.scene.next_scene:
                self.scene = self.scene.next_scene
                self.scene.next_scene = self.scene

            # 3. 描画
            self.scene.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
