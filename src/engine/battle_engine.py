import random
import math

class BattleEngine:
    def __init__(self, allies, enemies,data_manager):
        self.allies = allies
        self.enemies = enemies
        self.data_manager = data_manager
        self.all_members = allies + enemies
        self.turn_counts = {char: 0 for char in self.all_members} # 各キャラの行動回数(x)

    def calculate_likelihood(self, char):
        """仕様書に基づく行動抽選率の算出"""
        x = 2 # 補正項（調整用）
        n = self.turn_counts[char] + 1 # フェーズ内での行動回数
        
        # 0徐算対策
        x = max(0.1,x)

        # AGI * (1/x)^n - 1 (結果切り捨て)
        likelihood = char.agi // math.pow(x,(n-1))
        return max(0, likelihood)

    def select_next_actor(self):
        """重み付き乱数による行動主体の選別[cite: 1]"""
        weights = []
        candidates = []

        for char in self.all_members:
            if char.hp > 0: # 生存者のみ
                w = self.calculate_likelihood(char)
                weights.append(w)
                candidates.append(char)

        if sum(weights) <= 0:
            return None # フェーズ終了[cite: 1]

        # 重みに基づいて1人選出
        selected = random.choices(candidates, weights=weights, k=1)[0]
        self.turn_counts[selected] += 1 # 行動回数を加算
        return selected

    def resolve_action(self, actor):
        """アクションの決定と対象の選定"""
        
        # 1. アクションの重み設定
        # 攻撃: 20, 防御: 10, サボり: max(0, 30 - 忠誠度)
        slacking_weight = max(0, 30 - actor.loyalty)
        
        action_options = ["攻撃", "防御", "サボり"]
        weights = [20, 10, slacking_weight]
        
        # 2. アクションの抽選（重み付きランダム）
        chosen_action = random.choices(action_options, weights=weights, k=1)[0]
        
        # 3. アクション内容に応じた処理とログ生成
        log_msg = ""
        
        if chosen_action == "攻撃":
            # 生存している敵をリストアップ
            targets = [e for e in (self.enemies if actor.side == "ally" else self.allies) if e.hp > 0]
            if targets:
                target = random.choice(targets)
                log_msg = f"{actor.name}: {target.name}に攻撃"
            else:
                log_msg = f"{actor.name}: 攻撃対象がいないため待機"
                
        elif chosen_action == "防御":
            log_msg = f"{actor.name}: 防御している"
            
        elif chosen_action == "サボり":
            log_msg = f"{actor.name}: サボっている"
            
        return log_msg