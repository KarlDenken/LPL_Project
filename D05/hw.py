'''
1. Find the Narcissistic number

Version: 0.1
Author: Karl
'''

for number in range(100, 1000):
    bit = number % 10
    top = (number % 100) // 10
    hundred = number // 100
    # print(f'{hundred} {top} {bit}')
    if bit**3 + top**3 + hundred**3 == number:
        print(f'{number} is a Narcissistic number')


'''
2. Find the perfect number
The perfect numer is limited in 1000000
Version: 0.1
Author: Karl
'''
upper_bound = 10000
from math import sqrt

for number in range(1, upper_bound):
    sum = 0
    for factor in range(1, int(sqrt(number) + 1)):
        if number % factor == 0:
            sum += factor
            if factor > 1 and number / factor != factor:
                sum += number / factor
    if sum == number:
        print(f'{number} is a perfect number')

'''
3. Chicken

Version: 0.1
Author: Karl
'''

for male in range(0, 20):
    for female in range(0, 34):
        if male * 5 + female * 3 + (100 - male - female) / 3 == 100:
            print(f'You can by {male} M, {female} F and {100 - male - female} Little')

'''
Craps Gambling:

Version: 0.1
Author Karl
'''
from random import randint

counter = 0
record = -1

while True:
    dice_1 = randint(1, 6)
    dice_2 = randint(1, 6)
    counter += 1
    print(f'{counter} roll, dice 1 = {dice_1}, dice_2 = {dice_2}')
    print
    dice_sum = dice_1 + dice_2
    if (record < 0 and dice_sum == 7 or dice_sum == 11) or (record > 0 and dice_sum == record):
        print('You Win!')
        break
    elif (record < 0 and dice_sum == 2 or dice_sum == 3 or dice_sum == 12) or (record > 0 and dice_sum == 7):
        print('You Lose!')
        break
    else:
        record = dice_sum
