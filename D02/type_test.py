'''
Use the variable to store the data and do calculation

Version: 0.1
Author: Karl
'''

a = 321
b = 123
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

'''
Use `input` to do input
use `int()` to change the type

Version: 0.1
Author: Karl
'''

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %d' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

'''
use `type` to check the type

Version: 0.1
Author: Karl
'''

a = 100
b = 12.345
c = 1 + 5j
d = 'hello world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
