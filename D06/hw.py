def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x, y):
    return x * y // gcd(x, y)

def is palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False


if __name__ == '__main__':
    x = int(input('x = '))
    y = int(input('y = '))
    print(f'the gcd of {x} and {y} is {gcd(x, y)}')
    print(f'the lcm of {x} and {y} is {lcm(x, y)}')
