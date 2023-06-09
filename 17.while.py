# -*- coding: utf-8 -*-
n = 0
while n < 3:
    print(n)
    n += 1
"""
0
1
2
"""

n = 0
while True:
    print(n)
    n += 1
    if not (n < 3):
        # breakが実行される場合、ループから抜き出す
        break
"""
0
1
2
"""
