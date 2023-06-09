# -*- coding: utf-8 -*-

# 交差（共通部分）：&演算子またはintersection()メソッドを使用して、2つのセットの交差部分を計算します。
set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection = set1 & set2
print(intersection)  # 出力: {2, 3}

# またはintersection()メソッドを使用する
intersection = set1.intersection(set2)
print(intersection)  # 出力: {2, 3}

# 和（合併）：|演算子またはunion()メソッドを使用して、2つのセットの和を計算します。
set1 = {1, 2, 3}
set2 = {2, 3, 4}
union = set1 | set2
print(union)  # 出力: {1, 2, 3, 4}

# またはunion()メソッドを使用する
union = set1.union(set2)
print(union)  # 出力: {1, 2, 3, 4}

# 差（除外）：-演算子またはdifference()メソッドを使用して、2つのセットの差を計算します。
set1 = {1, 2, 3}
set2 = {2, 3, 4}
difference = set1 - set2
print(difference)  # 出力: {1}

# またはdifference()メソッドを使用する
difference = set1.difference(set2)
print(difference)  # 出力: {1}

# 対称差（排他的論理和）：^演算子またはsymmetric_difference()メソッドを使用して、2つのセットの対称差（片方のセットにのみ存在する要素）を計算します。
set1 = {1, 2, 3}
set2 = {2, 3, 4}
symmetric_difference = set1 ^ set2
print(symmetric_difference)  # 出力: {1, 4}

# またはsymmetric_difference()メソッドを使用する
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)  # 出力: {1, 4}

# 包含関係：<=、>=、<、>、==、issubset()メソッド、issuperset()メソッドを使用して、2つのセット間の包含関係を判定します。
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4}
print(set1 <= set2)  # 出力: True
print(set1 >= set2)  # 出力: False

# またはissubset()メソッドとissuperset()メソッドを使用する
print(set1.issubset(set2))  # 出力: True

print(set2.issuperset(set1))  # 出力: True
