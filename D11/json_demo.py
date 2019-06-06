import json

def main():
    mydict = {
        'name': 'Karl',
        'age': 22,
        'qq': 1234567,
        'friends': ['DD', 'FF'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320},
        ]
    }
    try:
        with open('data_2.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
            result = json.dumps(mydict)
    except IOError as e:
        print(e)
    print('Data saved')
    print(result)

if __name__ == '__main__':
    main()
