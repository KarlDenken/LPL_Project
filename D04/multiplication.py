'''
Get the tabular for the multiplication

Version: 0.1
Author: Karl
'''

for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}*{i}={i*j}', end = '\t')
    print()
