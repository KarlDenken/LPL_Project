# prices = {
#   'AAPL': 191.88,
#   'GOOG': 1186.96,
#   'IBM': 149.24,
#   'ORCL': 48.44,
#   'ACN': 166.89,
#   'FB': 208.09,
#   'SYMC': 21.29
# }
# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)
#
# names = ['Ada', 'Bob', 'Cassy', 'Darwin']
# courses = ['Math', 'Chinese', 'English']
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#   for col, course in enumerate(courses):
#     scores[row][col] = float(input(f'Please input score of {name} for {course}:'))
#     print(scores)

def my_range(start, end):
    for n in range(start, end):
        result = yield 2*n + 1
        print(result)

def main():
    g1 = my_range(3, 6)
    print(g1.send(None))
    print(g1.send('Hello'))
    print(g1.send('World'))


if __name__ == '__main__':
    main()
