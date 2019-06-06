'''
Convert the fahrenheit to celsius
F = 1.8C + 32

Version: 0.1
Author: Karl
'''
f = float(input('Please input the degree fahrenheit '))
c = (f - 32) / 1.8
print('%.1f degree fahrenheit = %.1f degree celsius' % (f, c))

'''
Input the radius and calculate the circumference and area

Version: 0.1
Author: Karl
'''
import math

radius = float(input('Please input the radius of the circle: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('Circumference: %.2f' % perimeter)
print('Area: %.2f ' % area)


'''
Check if the year is leap, True if yes and False if no

Version: 0.1
Author: Karl
'''

year = int(input('Please input the year:'))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(is_leap)
