class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age >= 16:
            print(f'{self._name} is playing Chessboard game')
        else:
            print(f'{self._name} is playing Gambling game')

def main():
    person = Person('Wang Dachui', 22)
    person.play()
    person.age = 11
    person.play()
    print(person.name)
    # Will have error if you do person.name since there is no setter for it
    # person.name = 'DD'


if __name__ == '__main__':
    main()
