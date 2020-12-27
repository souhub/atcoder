sx, sy, gx, gy = map(int, input().split())
x = float((gx*sy + gy*sx)/(gy + sy))
print(x)

# sympy 使用できなかったが理由不明で調査中
# 可能性としては
# ・サードパーティーライブラリの仕様が許可されていない
# ・なにか特別なライブラリ登録などが必要
