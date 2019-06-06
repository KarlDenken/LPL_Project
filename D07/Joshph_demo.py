def main():
    persons = [True] * 30
    counter, index, num = 0, 0, 0
    while counter < 15:
        if persons[index]:
            # print(f'{index} saved')
            num += 1
            if num == 9:
                persons[index] = False
                print(f'{index} dead')
                counter += 1
                num = 0
        index += 1
        index %= 30
    for person in persons:
        print('Cristian' if person else 'Non-Crisitian', end=" ")


if __name__ == '__main__':
    print('main')
    main()
