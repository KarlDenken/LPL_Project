class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name} is studying {course_name}')

    def watch_av(self):
        if self.age < 18:
            print(f'{self.name} is able to watch Tom and Jerry')
        else:
            print(f'{self.name} is able to watch porn')


def main():
    stu1 = Student('Jessi', 28)
    stu1.study('Python')
    stu1.watch_av()

    stu2 = Student('Didi', 14)
    stu2.study('Math')
    stu2.watch_av()


if __name__ == "__main__":
    main()
