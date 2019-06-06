from random import randint
from time import time, sleep

def download_file(filename):
    print(f'Starting to download \"{filename}\" ...')
    time_to_sleep = randint(5, 10)
    sleep(time_to_sleep)
    print(f'{filename} to downloaded, use {time_to_sleep}s')
    print('*' * 50)

def main():
    start = time()
    download_file('Learning from Python')
    download_file('How to read a book')
    end = time()
    print(f'Total uses {end - start}s')

if __name__ == '__main__':
    main()
