from functools import lru_cache

MENUS = [400, 350, 300]

def get_payment_combinations(target, n250, n150, n100):
    valid_combos = []
    for u250 in range(n250 + 1):
        for u150 in range(n150 + 1):
            for u100 in range(n100 + 1):
                if u250 * 250 + u150 * 150 + u100 * 100 == target:
                    valid_combos.append((u250, u150, u100))
    return valid_combos

# メモ化用の辞書。最大値だけでなく、「その時の最適な選択」も保存する
# 構造: {(n250, n150, n100): (max_meals, chosen_menu, (u250, u150, u100))}
dp_table = {}

def solve_dp(n250, n150, n100):
    state = (n250, n150, n100)
    if state in dp_table:
        return dp_table[state][0]
    
    if n250 == 0 and n150 == 0 and n100 == 0:
        dp_table[state] = (0, None, None)
        return 0
    
    max_count = 0
    best_menu = None
    best_combo = None
    
    for price in MENUS:
        combos = get_payment_combinations(price, n250, n150, n100)
        for u250, u150, u100 in combos:
            count = 1 + solve_dp(n250 - u250, n150 - u150, n100 - u100)
            if count > max_count:
                max_count = count
                best_menu = price
                best_combo = (u250, u150, u100)
                
    dp_table[state] = (max_count, best_menu, best_combo)
    return max_count

# 経路を復元して出力する関数
def print_history(n250, n150, n100):
    solve_dp(n250, n150, n100) # DP実行
    
    curr_250, curr_150, curr_100 = n250, n150, n100
    meal_count = 1
    
    print(f"--- 最適食事計画（合計 {dp_table[(n250, n150, n100)][0]} 回） ---")
    
    while True:
        state = (curr_250, curr_150, curr_100)
        _, menu, combo = dp_table[state]
        
        if menu is None:
            break
            
        u250, u150, u100 = combo
        print(f"【{meal_count}食目】 {menu}円のメニュー")
        print(f"  └ 支払いの内訳: [250円券]×{u250}枚, [150円券]×{u150}枚, [100円券]×{u100}枚")
        
        # 状態を更新
        curr_250 -= u250
        curr_150 -= u150
        curr_100 -= u100
        meal_count += 1

# 実行
print_history(20, 20, 20)
