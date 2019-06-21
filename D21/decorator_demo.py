def debug(func):
    def wrapper():
        print(f'[DEBUG]: enter {func.__name__}')
        return func()
    return wrapper

@debug
def say_hello():
    print("hello")

@debug
def say_goodbye():
    # print('Goodbye')
    print('Hello') # bug here



if __name__ == '__main__':
    say_hello()
    say_goodbye()
