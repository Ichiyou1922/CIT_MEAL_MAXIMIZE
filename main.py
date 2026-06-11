from functools import lru_cache

# 学食の価格リスト
MENUS = [400, 350, 300]
# 券の額面
TICKET_VALUES = [250, 150, 100]

# 指定された金額(target)を、手持ちの券(n250, n150, n100)から「ぴったり」支払う組み合わせを全列挙する関数
def get_payment_combinations(target, n250, n150, n100):
    valid_combos = []
    # 各券を何枚使うかループ
    for u250 in range(n250 + 1):
        for u150 in range(n150 + 1):
            for u100 in range(n100 + 1):
                if u250 * 250 + u150 * 150 + u100 * 100 == target:
                    valid_combos.append((u250, u150, u100))
    return valid_combos

@lru_cache(maxsize=None)
def max_meals(n250, n150, n100):
    # ベースケース: 券がなくなったらこれ以上食べられない
    if n250 == 0 and n150 == 0 and n100 == 0:
        return 0
    
    max_count = 0
    
    # 3つのメニューそれぞれについて試す
    for price in MENUS:
        # その価格を支払うための券の組み合わせを取得
        combos = get_payment_combinations(price, n250, n150, n100)
        for u250, u150, u100 in combos:
            # 券を消費して再帰呼び出し。食事回数を+1する
            count = 1 + max_meals(n250 - u250, n150 - u150, n100 - u100)
            if count > max_count:
                max_count = count
                max_250 = u250
                max_150 = u150
                max_100 = u100
    return max_count, max_250, max_150, max_100

# 初期状態：各20枚
initial_250 = 20
initial_150 = 20
initial_100 = 20

result, max_250, max_150, max_100 = max_meals(initial_250, initial_150, initial_100)
print(f"最大食事回数: {result} 回/250: {max_250}/150: {max_150}/100: {max_100}")
