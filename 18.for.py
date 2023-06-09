# -*- coding: utf-8 -*-
for i in range(3):
    print(i)
print()
'''
0
1
2
'''

for i in range(1, 2):
    print(i)
print()
'''
1
'''

for i in range(1, 5, 2):
    print(i)
print()
'''
1
3
'''

for i in range(5, 0, -2):
    print(i)
print()
'''
5
3
1
'''

for i in 'abcd':
    print(i)
print()
'''
a
b
c
d
'''

for i in [1, 2, 3]:
    print(i)
print()
'''
1
2
3
'''

for i in (1, 2, 3):
    print(i)
print()
'''
1
2
3
'''

d = {'k1': 'v1', 'k2': 'v2'}
for i in d:
    print(i)
print()
'''
k1
k2
'''

for i in d.keys():
    print(i)
print()
'''
k1
k2
'''

for i in d.values():
    print(i)
print()
'''
v1
v2
'''

for k, v in d.items():
    print(k, v)
'''
k1 v1
k2 v2
'''
