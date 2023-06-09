# -*- coding: utf-8 -*-
# リストの定義
my_list = [1, 2, 3, 2, 4, 1]
print(my_list)  # 出力: [1, 2, 3, 2, 4, 1]

# セットの定義
my_set = {1, 2, 3, 2, 4, 1}
print(my_set)  # 出力: {1, 2, 3, 4}

# リスト内の要素の順序を保持してアクセスする
print(my_list[0])  # 出力: 1

# セット内の要素の順序はランダムなので、インデックスでのアクセスはできない
try:
    print(my_set[0])
except TypeError as e:
    print(e)  # 'set' object is not subscriptable

# リストから要素を削除
my_list.remove(2)
print(my_list)  # 出力: [1, 3, 2, 4, 1]

# セットから要素を削除
my_set.remove(2)
print(my_set)  # 出力: {1, 3, 4}
