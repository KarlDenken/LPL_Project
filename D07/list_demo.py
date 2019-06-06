def main():
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2 = ['hello'] * 5
    print(list2)
    print(f'list1 lenght = {len(list1)}')
    print(list1[0])
    print(list1[4])
    print(list1[-1])
    print(list1[-3])

    list1[2] = 300
    print(list1)

    list1.append(200)
    list1.insert(1, 400)
    list1 += [1000, 2000]
    print(list1)
    print(len(list1))

    list1.remove(3)
    if 1000 in list1:
        list1.remove(1000)
    del list1[0]
    print(list1)
    list1.clear()
    print(list1)

def main_2():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['putaya', 'pear', 'mango']

    print(fruits)
    for fruit in fruits:
        print(fruit.title(), end = ' ' )
    print()
    fruits2 = fruits[1:4]
    print(fruits2)
    fruits3 = fruits[:]
    # if you write fruits3 = fruit, you only start a new reference
    print(fruits3)
    fruits4 = fruit[-3:-1]
    print(fruits4)
    fruits5 = fruits[::-1]
    print(fruits5)

def main_3():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    print(list2)
    list3 = sorted(list1, reverse=True)
    list4 = sorted(list1, key=len)
    print(list3)
    print(list4)

    list1.sort(reverse=True)
    print(list1)

def main_4():
    import sys
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)
    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))
    print(f)

    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))
    print(f)
    for val in f:
        print(val)
        




if __name__ == "__main__":
    main_4()
