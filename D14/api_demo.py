url = 'https://restapi.amap.com/v3/weather/weatherInfo?city=110101&key=1681e460e5f967b8294dec26d403b273'

from time import time

import requests

def main():
    resp = requests.get(url=url)
    data_model = resp.json()
    status = data_model['status']
    if status == '0':
        print('API non accessible currently')
        return
    else:
        data = data_model['lives'][0]
        province = data['province']
        city = data['city']
        weather = data['weather']
        temperature = data['temperature']
        time = data['reporttime']
        print(f'{province}-{city}')
        print(f'{weather},{temperature}')
        print(f'Last update:{time}')
        print('*' * 50)


if __name__ == '__main__':
    main()
