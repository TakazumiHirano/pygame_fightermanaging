import random
import math

class BattleEngine:
    def __init__(self, allies, enemies):
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
        """アクションの決定（忠誠度や信頼度によるブレ）[cite: 1]"""
        # ここに「忠誠度が低いとサボる」「好感度が高いと庇う」などのロジックを入れる[cite: 1]
        log = f"{actor.name} の行動！"
        return log
