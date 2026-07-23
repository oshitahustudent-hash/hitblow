# hint_system.py

class HintManager:
    def __init__(self):
        self.hint_available = True  # ヒントの使用権
        self.last_guess = None      # 直前のプレイヤーの入力を記録

    def get_hint(self, secret: str) -> str:
        """ヒントを生成し、使用権を消費する"""
        if not self.hint_available:
            return "【システム】エラー: ヒントはすでに使用されています。"
        if self.last_guess is None:
            return "【システム】エラー: まだ一度も入力していません。まずは最初の推測を入力してください。"
        
        # 各桁の Higher / Lower / Equal 判定
        hint_chars = []
        for i in range(len(secret)):
            g_digit = int(self.last_guess[i])
            t_digit = int(secret[i])
            
            if g_digit < t_digit:
                hint_chars.append("H")  # 入力より正解が大きい (Higher)
            elif g_digit > t_digit:
                hint_chars.append("L")  # 入力より正解が小さい (Lower)
            else:
                hint_chars.append("=")  # ピタリ一致 (Equal)
                
        # ヒントを使ったら使用不可にする
        self.hint_available = False
        
        hint_str = "".join(hint_chars)
        return (
            f"💡 [ヒント] 直前の入力 '{self.last_guess}' に対する結果: {hint_str}\n"
            f"   （H: 正解の方が大きい / L: 正解の方が小さい / =: 一致）"
        )

    def update_last_guess(self, guess: str):
        """直前の有効な入力を保存する"""
        self.last_guess = guess

    def show_status(self):
        """ヒント使用権の有無を出力する"""
        status = "○ (使用可能)" if self.hint_available else "× (使用済み)"
        print(f"ヒント使用権: [{status}]")


# 外部からはこのインスタンスをインポートして使い回します（シングルトン）
hint_manager = HintManager()