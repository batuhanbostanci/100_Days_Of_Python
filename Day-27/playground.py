# def add(*args):
#     sum_nums = 0
#     for n in args:
#         sum_nums += n
#     print(sum_nums)
#
# add(1, 2, 3, 4, 5, 6)

def calculate(n, **kwargs):

    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

car = Car(make="Nissan", model="GR-R")

print(car.model)
