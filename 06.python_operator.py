print('1 + 2 =', 1 + 2)
print('1 - 2 =', 1 - 2)
print('2 * 3 =', 2 * 3)
print('6 / 2 =', 6 / 2)
print('11 % 3 =', 11 % 3)
print('2 ** 10 =', 2 ** 10)
print('11 // 3 =', 11 // 3)

print('1 == 1 =', 1 == 1)
print('1 != 1 =', 1 != 1)
print('2 > 3 =', 2 > 3)
print('2 < 3 =', 2 < 3)
print('2 >= 2 =', 2 >= 2)
print('2 <= 3 =', 2 <= 3)

n = 5
print('after =5, n =', n)

n = 5
n += 3
print('after +=3, n =', n)

n = 5
n -= 3
print('after -=3, n =', n)

n = 5
n *= 3
print('after *=3, n =', n)

n = 5
n /= 3
print('after /=3, n =', n)

n = 5
n %= 3
print('after %=3, n =', n)

n = 5
n **= 3
print('after **=3, n =', n)

n = 5
n //= 3
print('after //=3, n =', n)

print('True and True =', True and True)
print('True and False =', True and False)
print('False and True =', False and True)
print('False and False =', False and False)

print('True or True =', True or True)
print('True or False =', True or False)
print('False or True =', False or True)
print('False or False =', False or False)

print(not True)
print(not False)

n1 = 0b1100
n2 = 0b1010

print(f'{n1 & n2:5b}')
print(f'{n1 | n2:5b}')
print(f'{n1 ^ n2:5b}')
print(f'{~n1:5b}')
print(f'{n1 << 1:5b}')
print(f'{n1 >> 1:5b}')
