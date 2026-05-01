# src/scenes/__init__.py

# エンジンから基底クラスを連れてくる
from src.engine.scene_base import SceneBase

# 各シーンを公開する
from .title_scene import TitleScene
from .battle_scene import BattleScene
from .settings_scene import SettingsScene

# 外部から「from src.scenes import *」とした時に公開するリスト（任意）
__all__ = ["TitleScene", "BattleScene", "SettingsScene"]
