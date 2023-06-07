# 错误示例：没有声明编码方式
print("你好，世界！")

text = '0123456'
# index'0123456'

print(text[:])  # 0123456
print(text[1:-1])  # 12345
print(text[3:])  # 3456
print(text[:3])  # 012
print(text[:-3])  # 0123
print(text[2:4])  # 23
print(text[::2])  # 0246
print(text[::-1])  # 6543210
print(text[4:2:-1])  # 43

text = '0123456'
# index'0123456'
print(text[0])  # 0
print(text[1])  # 1
print(text[2])  # 2
print(text[-1])  # 6
print(text[-2])  # 5
