import pygame


class SceneController:
    """シーンの登録と遷移を管理するコントローラ"""

    def __init__(self):
        self.scenes_registry = {}  # "title": TitleScene のような辞書
        self.current_scene = None
        self.current_scene_name = None  # 現在のシーン名を保持
        self.history = []               # 遷移履歴を保存するスタック

    def register(self, name, scene_class):
        """シーンを名前で登録する"""
        self.scenes_registry[name] = scene_class

    def request_change(self, name, use_history=True, **kwargs):
        """
        シーン切り替えリクエストを受け取り、インスタンスを生成する
        name: 遷移先の名前
        use_history: 履歴に保存するかどうか
        """
        # 現在のシーン名を履歴に追加（"settings"へ行く時など）
        if use_history and self.current_scene_name:
            self.history.append(self.current_scene_name)

        if name in self.scenes_registry:
            scene_class = self.scenes_registry[name]
            # 新しいシーンをインスタンス化（controllerを自分自身として渡す）
            self.current_scene_name = name
            self.current_scene = scene_class(self, **kwargs)
        else:
            print(f"Error: Scene '{name}' is not registered.")

    def request_back(self, **kwargs):
        """履歴を一つ遡って戻る"""
        if self.history:
            prev_name = self.history.pop()  # 最後の履歴を取り出す
            # 戻る動作自体は履歴に残さない(use_history=False)
            self.request_change(prev_name, use_history=False, **kwargs)
        else:
            # 履歴がない場合はデフォルトでタイトルへ
            self.request_change("title", use_history=False)


class SceneBase:
    """すべての画面の親となるクラス"""

    def __init__(self, controller):
        self.controller = controller

    def update(self):
        pass

    def draw(self, screen):
        pass

    def handle_event(self, event):
        pass

    def terminate(self):
        pass
