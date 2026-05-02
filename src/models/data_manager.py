import json
import os


class DataManager:
    def __init__(self):
        self.character_data = {}

        # このファイルの場所を基準に、プロジェクトのルートディレクトリを特定する
        # src/models/data_manager.py から見て 2つ上の階層がルート
        self.base_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(__file__)))

        self.load_all_data()

    def load_all_data(self):
        """JSONファイルを読み込む"""
        # ルートディレクトリからの絶対パスを組み立てる
        path = os.path.join(self.base_dir, "data",
                            "master_data", "characters.json")

        try:
            with open(path, "r", encoding="utf-8") as f:
                self.character_data = json.load(f)
        except FileNotFoundError:
            print(f"Error: {path} が見つかりません。")

    def get_character_params(self, char_id):
        """特定のキャラクターのパラメータを返す"""
        return self.character_data.get(char_id, {})
