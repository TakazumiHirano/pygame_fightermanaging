import json
import os


class DataManager:
    def __init__(self):
        self.character_data = {}

        # このファイルの場所を基準に、プロジェクトのルートディレクトリを特定する
        # src/models/data_manager.py から見て 2つ上の階層がルート
        self.base_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(__file__)))

        self.master_data = {}
        self.load_all_data()

    def load_all_data(self):
        """ 複数のJSONファイルを読み込む """
        # ルートディレクトリからの絶対パスを組み立てる
        for data_name in ["characters", "jobs", "traits"]:
            path = os.path.join(self.base_dir, "data",
                                "master_data", f"{data_name}.json")
            with open(path, "r", encoding="utf-8") as f:
                self.master_data[data_name] = json.load(f)

    def get_final_stats(self, char_id):
        """個体、職業、性格を合算して最終パラメータを算出する"""
        char = self.master_data["characters"].get(char_id, {})
        job = self.master_data["jobs"].get(char.get("job_id"), {})

        # 基礎値のセット
        final_agi = job.get("base_agi", 10)
        final_str = job.get("base_str", 10)
        final_vit = job.get("base_vit", 10)

        # 性格による補正（倍率をかける）
        for t_id in char.get("trait_ids", []):
            trait = self.master_data["traits"].get(t_id, {})
            final_agi *= trait.get("agi_mod", 1.0)
            final_str *= trait.get("str_mod", 1.0)
            final_vit *= trait.get("vit_mod", 1.0)  # 性格によるVIT補正[cite: 1]

        return {
            "name": char.get("name"),
            "agi": int(final_agi),
            "str": int(final_str),
            "vit": int(final_vit),
            "loyalty": char.get("loyalty", 50),
            "image_label": char.get("image_label")
        }

    def get_character_params(self, char_id):
        """特定のキャラクターのパラメータを返す"""
        return self.character_data.get(char_id, {})
