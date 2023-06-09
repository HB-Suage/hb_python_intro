# -*- coding: utf-8 -*-
# リストの定義
my_list = [1, 2, 3, 4]
print(my_list)  # 出力: [1, 2, 3, 4]

# タプルの定義
my_tuple = (1, 2, 3, 4)
print(my_tuple)  # 出力: (1, 2, 3, 4)

# リスト内の要素の変更
my_list[0] = 5
print(my_list)  # 出力: [5, 2, 3, 4]

# タプル内の要素を変更しようとするとエラーが発生します
try:
    my_tuple[0] = 5
except TypeError as e:
    print(e)  # 'tuple' object does not support item assignment

# リストに要素を追加
my_list.append(5)
print(my_list)  # 出力: [5, 2, 3, 4, 5]

# タプルに要素を追加しようとするとエラーが発生します
try:
    my_tuple.append(5)
except AttributeError as e:
    print(e)  # 'tuple' object has no attribute 'append'

# リストから要素を削除
my_list.pop(0)
print(my_list)  # 出力: [2, 3, 4, 5]

# タプルから要素を削除しようとするとエラーが発生します
try:
    my_tuple.pop(0)
except AttributeError as e:
    print(e)  # 'tuple' object has no attribute 'pop'
