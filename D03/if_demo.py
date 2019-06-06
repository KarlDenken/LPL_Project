# '''
# User authentication
#
# Version: 0.1
# Author: Karl
# '''
#
# username = input('Please input the username: ')
# import getpass
# password = getpass.getpass('Please input the password: ')
#
# if username == 'admin' and password == '123456':
#     print('User authentified')
# else:
#     print('Authentification failed')

'''
Piecewise function
        3x - 5 (x > 1)
f(x) =  x + 2 (-1 <= x <=1)
        5x + 3 (x < -1)
Version: 0.1
Author: Karl
'''
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f '% (x, y))
