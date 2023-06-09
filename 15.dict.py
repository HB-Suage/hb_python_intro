# -*- coding: utf-8 -*-
# 辞書の作成
person = {
    "名前": "太郎",
    "年齢": 20,
    "性別": "男性",
}

name = person["名前"]  # キー"名前"に対応する値を取得
print(name)  # 太郎
age = person["年齢"]  # キー"年齢"に対応する値を取得
print(age)  # 20

person["職業"] = "学生"  # キー"職業"と値"学生"のペアを追加
print(person.get('職業'))  # 学生
person["年齢"] = 21  # キー"年齢"に対応する値を変更
print(person.get('年齢'))  # 21

del person["性別"]  # キー"性別"に対応する要素を削除

keys = person.keys()  # 辞書のキーを取得
print(keys)  # dict_keys(['名前', '年齢', '職業'])

values = person.values()  # 辞書の値を取得
print(values)  # dict_values(['太郎', 21, '学生'])

items = person.items()  # 辞書のキーと値のペアを取得
print(items)  # dict_items([('名前', '太郎'), ('年齢', 21), ('職業', '学生')])

# dict['key']とdict.get('key')の違い
# 存在しないキーをアクセスしたい場合
try:
    print(person['TEL'])
except Exception as e:
    print(type(e), e)  # <class 'KeyError'> 'TEL'

print(person.get('TEL'))  # None
