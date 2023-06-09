# -*- coding: utf-8 -*-
def greet(name):
    print("こんにちは、" + name + "さん！")


greet("太郎")  # 関数呼び出し


def is_ip(ip):
    try:
        split_ip = ip.split('.')
        if len(split_ip) != 4:  # IP地址由四个数字组成
            return False
        for num in split_ip:
            if not num.isdigit():  # 检查每个数字是否为整数
                return False
            if not 0 <= int(num) <= 255:  # 检查每个数字是否在有效范围内
                return False
        return True
    except:  # noqa
        return False


print(is_ip('192.168.0.1'))  # True
print(is_ip('192.168.500.1'))  # False
print(is_ip('Hello'))  # False


def add(a: int, b: int) -> int:
    return a + b


print(add(1, 2))  # 3

