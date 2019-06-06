import re

def main():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    What is your phone number 1421343143234, My phone is 13511111111, not 15600000000, nor 110 or 119. Danies's phone is 15600000000
    '''
    my_list = re.findall(pattern, sentence)
    print(my_list)
    print('HHH'.center(50, '-'))
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('H'.center(50, '-'))
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == '__main__':
    main()
