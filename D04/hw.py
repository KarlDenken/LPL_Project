# '''
# Determine whether a number is prime
#
# Version: 0.1
# Author: Karl
# '''
#
# from math import sqrt
#
# num = int(input('An integer:'))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print(f'{num} IS PRIME')
# else:
#     print(f'{num} IS NOT PRIME')

# '''
# Get the factor
#
# Version: 0.1
# Author: Karl
# '''
#
# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
#     x, y = y, x
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print(f'{x} and {y} has the MCD is {factor}')
#         print(f'{x} and {y} has the MCM is {x * y // factor}')
#         break

row = int(input('Please enter the row:'))
for i in range(row):
    for _ in range(i + 1):
        print('*', end = '')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end = '')
        else:
            print('*', end = '')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ' , end = '')
    for _ in range(2 * i + 1):
        print('*', end = '')
    print()
