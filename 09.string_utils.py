# -*- coding: utf-8 -*-
string = 'www.hearbest.jp'
# index   000000000011111
# index   012345678901234

# ドット(.)を区切り文字として文字列を分割する
print(string.split('.'))  # ['www', 'hearbest', 'jp']

# ドット(.)を区切り文字として最初の一つだけ文字列を分割する
print(string.split('.', 1))  # ['www', 'hearbest.jp']

# ドット(.)の数を数える
print(string.count('.'))  # 2

# 'w'の数を数える
print(string.count('w'))  # 3

# ドット(.)をアットマーク(@)に置き換える
print(string.replace('.', '@'))  # www@hearbest@jp

# 'j'の最初のインデックスを検索する
print(string.find('j'))  # 13

# ドット(.)を区切り文字として、右から最初の一つだけ文字列を分割する
print(string.rsplit('.', 1))  # ['www.hearbest', 'jp']

# ドット(.)の最後のインデックスを検索する
print(string.rfind('.'))  # 12

# 文字列を左寄せして幅20にする
print(string.ljust(20))  # www.hearbest.jp

# 文字列を左寄せして幅20にし、余白をアスタリスク(*)で埋める
print(string.ljust(20, '*'))  # www.hearbest.jp*****

# 文字列を右寄せして幅20にする
print(string.rjust(20))  # www.hearbest.jp

# 文字列を右寄せして幅20にし、余白をハッシュ記号(#)で埋める
print(string.rjust(20, '#'))  # #####www.hearbest.jp
