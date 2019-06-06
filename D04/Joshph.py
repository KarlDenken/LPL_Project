def main():
    print('Start')
    persons = [True] * 30
    counter, index, num = 0, 0, 0
    while counter < 15:
        if persons[index]:
            num += 1
            print(f'index = {index}, you are saved')
            if num == 9:
                persons[index] == False
                print(f'index = {index}, you are sacrifized')
                counter += 1
                num = 0
        index += 1
        index %= 30

    for person in persons:
        print('Cristian' if person else 'Non Crisitian')


if __name__ == '__main__':
    print('Start 1')
