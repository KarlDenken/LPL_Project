'''
We assume there is a bag with maxmum volumn as 20kg. The following is the content with its weight and price. You have to take as many objects as possible to get the value maximum. To get better result, we want to gave the most valuable object.
'''

class Thing(object):

    def __init__(self, name, price, weight):
        self._name = name
        self._price = price
        self._weight = weight

    @property
    def value(self):
        return self._price / self._weight

    @property
    def price(self):
        return self._price

    @property
    def weight(self):
        return self._weight

    @property
    def name(self):
        return self._name

def input_things():
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)

def main():
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_things()))
        # Adding * in front of a list/tuple/dic will split the list/tuple/dic into single elements
        all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing._weight <= max_weight:
            print(f'Thief has stolen {thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'Total value {total_price} dollars')


if __name__ == '__main__':
    main()
