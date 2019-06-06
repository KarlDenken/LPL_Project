def main():
    str1 = 'hello world!'
    # Get the len
    print(len(str1))
    # Get the captalized
    print(str1.capitalize())
    # Get the all upper case
    print(str1.upper())
    # Find the location
    print(str1.find('or'))
    print(str1.find('shit'))
    print(str1.index('or'))
    # print(str1.index('shit'))
    # Check if startwith
    print(str1.startswith('He'))
    print(str1.startswith('hel'))
    # Check if end with
    print(str1.endswith('!'))
    # center the string
    print(str1.center(50, '*'))
    print(str1.rjust(50, ' '))

    str2 = 'abc12345'
    print(str2[2])

    print(str2[2:5]) # the last index is not included, just like range
    print(str2[2:])
    print(str2[2::2])
    print(str2[::-1])
    print(str2[-3:-1])

    print(str2.isdigit())
    print(str2.isalpha())
    print(str2.isalnum())

    str3 = '   jackfreud@126.com   '
    print(str3)
    print(str3.strip())

if __name__ == "__main__":
    main()
