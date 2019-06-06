import os
import time
import random

def main_1():
    content = '  Welcome to Shenzhen  '
    while True:
        # Clean the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        print(content)
        time.sleep(0.2)
        # sleep 200 ms
        content = content[1:] + content[0]

def generate_code(code_len=4):
    '''
    generate verified code with code len

    : param code_len: code lenth
    : return: random verified code
    '''
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


def get_suffix(filename, has_dot=False):
    '''
    Get the suffix of the file

    :param filename: the filename
    :param has_dot: whether the dot is need in the returned suffix
    :return : the suffix
    '''
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return


def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2, m1 = m1, x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, date):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date

if __name__ == '__main__':
    print(which_day(2019, 5, 23))
