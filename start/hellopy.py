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

# list / tuple

friends = ['doudou', 'keke', 'huhu']
friends
len(friends)

friends[1]
friends[-1]

friends.append('zz')
friends.insert(1, 'hh')
friends.pop()
friends.pop(1)

friends[1] = 'zzh'

wth = ['wt', 12, True]
wth

lType =  ['python', 'java', ['asp', 'php'], 'scheme']
lType
len(lType)

L = []
len(L)

# >>> friends = ['doudou', 'keke', 'huhu']
# >>> friends
# ['doudou', 'keke', 'huhu']
# >>> len(friends)
# 3
# >>> friends[1]
# 'keke'
# >>> friends[-1]
# 'huhu'
# >>> friends.append('zz')
# >>> friends.insert(1, 'hh')
# >>> friends.pop()
# 'zz'
# >>> friends.pop(1)
# 'hh'
# >>> friends[1] = 'zzh'
# >>> wth = ['wt', 12, True]
# >>> wth
# ['wt', 12, True]
# >>> lType =  ['python', 'java', ['asp', 'php'], 'scheme']
# >>> lType
# ['python', 'java', ['asp', 'php'], 'scheme']
# >>> len(lType)
# 4
# >>> L = []
# >>> len(L)
# 0

exTuple = ('bu', 'ke', 'xiu', 'gai')
t = (1,)
t
# Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。
# list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。

# 条件判断
# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:
# age = int(input('Input your age: '))
age = 23
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

#循环
names = ['Michael', 'doudou', 'huhu']
for name in names:
    print(name)

list(range(4))
sum = 0;
for x in range(4):
  sum += x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。
# 特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。

#使用dict和set
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']

d.pop('Bob')

d.get('Michael')

'Thomas' in d

d

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

s = set([1, 1, 2, 2, 3, 3])

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
# {2, 3}
s1 | s2
# {1, 2, 3, 4}

a = [12, 3, 45, 12, 1, 3, 4, 1, 45, 's', 'ds', 's', 'dd']
set(a)