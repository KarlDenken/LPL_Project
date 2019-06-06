import requests
import json

url = 'http://api.tianapi.com/txapi/rkl/?&key=APIKEY'

def main():
    resp = requests.get(url=url)
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()
