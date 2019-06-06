import re


def main():
    username = input('Please input the username: ')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('Please input valid username')
        return
    qq = input('Please input the QQ number: ')

    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('Please input valid qq')
        return

    if m1 and m2:
        print('Valid info')


if __name__ == "__main__":
    main()
