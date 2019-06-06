class Person(object):

    # The class can bind the 'name', 'age' and 'gender'
    # __slots__ = ('_name', '_age', '_gender')

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
    person._gender = 'Male'
    person._is_gay = 'True'

if __name__ == '__main__':
    main()
