import random

print(random.uniform(0, 1))

print({a: b for a, b in zip([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd'])})

a = range(1, 30, 3)
b = range(35, 50)
zipped = list(zip(a, b))
print(list(zip(*zipped)))

d = {'a': 6, 'b': 23}

def blah(a=1, b=2):
    print(a, b)

blah(**d)


def n_grams(tokens, n=1):
    return zip(*[tokens[i:] for i in range(n)])

print(list(n_grams([1, 2, 3, 4], 3)))


a = lambda x: x + 2

print(a(4))


a = lambda x: x[0] + x[1]

print(a([[1, 2, 3, 4], [1, 2, 3, 4]]))


square = lambda x: x / 2

print(list(map(square, [1, 2, 3, 4, 5, 6])))

sum = lambda x: x + x
multiply = lambda x: x * x

all_functions = [sum, multiply]

for i in range(1):
    print(list(map(lambda x: x(i), all_functions)))

def my_decorator_1(func):
    def incrementer(*args, **kwargs):
        val = func(args[0], args[1])
        return val + 1
    return incrementer

def my_decorator_2(func):
    def divide_by_2(*args, **kwargs):
        val = func(args[0], args[1])
        return val / 2
    return divide_by_2


@my_decorator_1
@my_decorator_2
def my_function(a, b):
    return a + b

print(my_function(1, 2))


