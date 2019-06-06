def main():
    try:
        with open('test.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('Cannot open the file')
    except LookupError:
        print('Uncooding error')
    except UnicodeDecodeError:
        print('Decoding Error')


if __name__ == '__main__':
    main()
