import pygame
import sys
from config.settings import *

class Game:
    def __init__(self):
        # Pygameの初期化
        pygame.init()
        # ウィンドウの作成
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        # フレームレート管理用の時計
        self.clock = pygame.time.Clock()
        self.is_running = True

    def run(self):
        """ゲームループ"""
        while self.is_running:
            self.handle_events()  # 入力処理
            self.update()         # データ更新
            self.draw()           # 描画処理
            self.clock.tick(FPS)  # FPSの固定

        pygame.quit()
        sys.exit()

    def handle_events(self):
        """イベント処理（入力やウィンドウ操作）"""
        for event in pygame.event.get():
            # 閉じるボタンが押された時
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        """ゲームロジックの更新（今は空っぽ）"""
        pass

    def draw(self):
        """画面描画"""
        self.screen.fill(COLOR_BLACK)  # 背景を黒で塗りつぶし
        
        # --- ここに描画処理を書いていく ---
        # サンプルとして文字を表示
        font = pygame.font.SysFont("notosanscjp", 32) # 環境に合わせて変更してください
        text = font.render("Press 'X' to Close Window", True, COLOR_WHITE)
        self.screen.blit(text, (50, 50))
        
        pygame.display.flip()  # 画面を更新

if __name__ == "__main__":
    game = Game()
    game.run()