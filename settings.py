# constants.pyから必要な定数をインポート
from constants import GAME_TIME, A_MASS, DAMPING_FACTOR

# 設定値の表示
print("Current Game Settings:")
print(f"Game Time: {GAME_TIME} seconds")
print(f"A Mass: {A_MASS}")
print(f"Damping Factor: {DAMPING_FACTOR}")

# 新しい設定値の入力
GAME_TIME = int(input("Enter game time (seconds): "))
A_MASS = int(input("Enter mass of particle A: "))
DAMPING_FACTOR = float(input("Enter damping factor: "))
