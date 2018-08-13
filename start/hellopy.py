#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 0x0011

if a > 0:
  print(a)
else:
  print(-a)

print('I\'m learning\nPython.')

print(r'''line1 'kk'
line2
line3''')

True

print(3 > 2)

True and True

True and False

False and False

True or False

False or False

5 > 3 or 1 > 3

not 1 > 3

if None or 0:
  print(5 > 2)
else:
  print('wtf')

a = 'doudou'
b = a
b = 'keke'
print('a:', a)
print('b:', b)

print(10 / 3)
print(14 // 3)
print(9 / 3)
print(14 % 3)

ord('0')

ord('a')

ord('A')

ord('z')

ord('中')

chr(66)

chr(20013)

chr(25991)

'\u4e2d\u6587'

x = b'ABC'

x

c = 'ABC'

'ABC'.encode('ascii')

'ABC'.encode('ascii') == x

'中文'.encode('utf-8')

b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

len('中文')

len(b'ABC')

len('中文'.encode('utf-8'))

len(b'\xe4\xb8\xad\xe6\x96\x87')

# 占位符	替换内容
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数

print('%s is the best - %d percent' % ('doudou', 100))

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
