# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
# #input_num = int(input("Your NUmber to Add: "))
# print(add(2,23,5,4))









def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

calculate(add=3, multiplu =4)


class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")
my_car = Car(model="Kantanka")

print(my_car.model)
