# '''
# HW 1: Inch to centimeter
#
# Version: 0.1
# Author: Karl
# '''
#
# value = float(input('Please input length: '))
# unit = input('Please input unit: ')
#
# if unit == 'in' or unit == 'inch':
#     print('%f inch = %f centimeter' % (value, value * 2.54))
# elif unit == 'cm' or unit == 'centimeter':
#     print('%f centimeter = %f inch' % (value, value / 2.54))
# else:
#     print('Invalid unit')

'''
Roll a dice

Version: 0.1
Author: Karl
'''

from random import randint
face = randint(1, 6)
if face == 1:
    result = 'Sing'
elif face == 2:
    result = 'Dance'
elif face == 3:
    result = 'Dog'
elif face == 4:
    result = 'push up'
elif face == 5:
    result = 'tongue twist'
else:
    result = 'joke'

print(result)


# '''
# Grade chage
#
# Version: 1.0
# Author: Karl
# '''
#
# score = float(input('Please input the score: '))
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'E'
#
# print('The corresponding grade is ', grade)

# '''
# Get three lines and calculate the perimeter and area
#
# Version: 0.1
# Author: Karl
# '''
#
# import math
#
#
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
#
# if a + b > c and a + c > b and b + c > a:
#     print('Perimeter: %f' % (a + b + c))
#     p = (a + b + c) / 2
#     area = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     print('area = %f' % (area))
# else:
#     print('Cannot form a triangle')

'''
Calculate the tax

Version: 0.1
Author: Karl
'''

frequence = int(input('How many times you have been to PCL this month: '))
salary = 200 * frequence
if salary > 800:
    payment = (salary - 800) * (1 - 0.2) + 800
else:
    payment = salary

print('Your payment this month is %d YUAN' % (payment))
