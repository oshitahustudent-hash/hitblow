"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""

from .core import judge, make_secret


def play(digits=4):
    secret = make_secret(digits)
    print(f"Hit & Blow（{digits} 桁・重複なし!）")

    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====
    import time
    from .score import score_manager

    start_time = time.time()
    score_manager.reset()

    tries = 0
    while True:
        print(" ")
        print(f"あと{10-tries}回")

        guess = input("予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====
        # 例:  from .hint import hint
        #      if guess == "h":
        #          print(hint(secret)); continue
        from .hint import hint_manager
        from .score import score_manager

        # 1. 入力直後に、ヒントの使用可能ステータスを表示する
        hint_manager.show_status()

        # 2. キーボード入力 'h' でヒント発動
        if guess == "h":
            score_manager.apply_hint_penalty()  # ★持ち点を1/2に減点
            print(hint_manager.get_hint(secret))
            continue

        # 3. エラーチェックを通過する「正常な入力」だった場合のみ、直前の入力として記憶する
        if len(guess) == digits and guess.isdigit():
            hint_manager.update_last_guess(guess)

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue

        tries += 1
        score_manager.deduct_guess()  # ★回答1回ごとに -100点

        if tries > 10:
            break

        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")

        if hit == digits:

            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====
            from .score import score_manager

            elapsed_time = time.time() - start_time
            print(f"経過時間：{elapsed_time:.1f}秒")
            print(f"最終スコア: {score_manager.get_score()} 点")

            print(f"正解！ {tries} 回で当たり（答え {secret}）")
            break
