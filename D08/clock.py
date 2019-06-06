import time

class Clock(object):

    def __init__(self, hour=0, minutes=0, second=0):
        self._hour = hour
        self._minute = minutes
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '{:02d}:{:02d}:{:02d}'.format(self._hour, self._minute, self._second)

def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        time.sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
