# -*- coding: utf-8 -*-
if True:
    print(True)  # 条件が真の場合にTrueを出力

l = [1, 2, 3]

if not l:
    print(l)  # リストが空の場合にリストを出力しない

url = r'https://www.hearbest.jp/'
if 'hearbest' in url:
    print(url)  # 'hearbest'がURLに含まれる場合にURLを出力

val = ''

if isinstance(val, int):
    print('int')
elif isinstance(val, bool):
    print('bool')
elif isinstance(val, str):
    print('str')  # str
else:
    print('Unknown')
