from threading import Thread
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
    p1 = Thread(target=download_file, args=('Learning from python',))
    p1.start()
    p2 = Thread(target=download_file, args=('How to read a book',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print(f'Total uses {end - start :.3f}s')

if __name__ == '__main__':
    main()
