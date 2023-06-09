# -*- coding: utf-8 -*-
class Person:
    def __init__(self, name):
        self.name = name  # 属性の定義

    def say_hello(self):
        print(f"こんにちは！私の名前は{self.name}です。")  # メソッドの定義


person1 = Person("太郎")  # Personクラスのインスタンス化
person1.say_hello()  # メソッドの呼び出し

person2 = Person("花子")
person2.say_hello()

person1.age = 10
print(person1.age)

"""
こんにちは！私の名前は太郎です。
こんにちは！私の名前は花子です。
10
"""


class MyClass:
    def public_method(self):
        print("This is a public method.")

    def __private_method(self):
        print("This is a private method.")


obj = MyClass()
obj.public_method()  # パブリックメソッドを呼び出し

try:
    obj.__private_method()  # プライベートメソッドを直接呼び出し
except AttributeError as e:
    print(e)

"""
This is a public method.
'MyClass' object has no attribute '__private_method'
"""


class MyClass:
    def public_method(self):
        print("This is a public method.")

    def __private_method(self):
        print("This is a private method.")


obj = MyClass()
obj._MyClass__private_method()

"""
This is a private method.
"""