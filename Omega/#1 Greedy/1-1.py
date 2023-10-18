# 거스름돈

import sys

n = int(sys.stdin.readline().rstrip())
count = 0
coin_order = [500, 100, 50, 10]

for coin in coin_order:
    count += n // coin
    n %= coin

print(count)