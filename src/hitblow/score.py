class ScoreManager:

    def __init__(self, initial_score: int = 1000):
        self.initial_score = initial_score
        self.score = initial_score

    def reset(self):
        """ゲーム開始時にスコアを初期化する"""
        self.score = self.initial_score

    def deduct_guess(self):
        """1回答える（推測する）たびに -100点"""
        self.score -= 100

    def apply_hint_penalty(self):
        """ヒントを使うと現時点での持ち点を1/2にする"""
        self.score //= 2

    def get_score(self) -> int:
        """現在のスコアを取得する"""
        return self.score


# 他のファイルから共有して使えるインスタンスを作成
score_manager = ScoreManager()