import pickle


def coroutine(f):
    gen = f()
    next(gen)
    return gen


def f():
    fn = open('test.txt', 'rt')
    for line in fn:
        try:
            yield line
        except GeneratorExit:
            fn.close()
            break

g = f()
print(next(g))
print(next(g))
print(next(g))
g.close()
# print(next(g))

g = f()
print(next(g))
# g.throw(ValueError)


class A:
    def __init__(self, f):
        self.f = f
        self.a = 1

    def __getstate__(self):
        print('Get state')
        d = self.__dict__.copy()
        del d['f']
        return d

    def __setstate__(self, state):
        print('Set state')
        self.__dict__ = state
        self.f = lambda x: 2 * x

a = A(lambda x: 2 * x)

print(vars(a))

s = pickle.dumps(a)
print(s)

b = pickle.loads(s)
print(vars(b))

with open('file.txt', 'at') as f:
    f.write('String\n')


class B:
    def __init__(self):
        self.a = 1

    def __enter__(self):
        print("enter")

    def __exit__(self, *args, **kwargs):
        print("exit")

with B():
    pass


class Multipliyer:
    def __init__(self, n):
        self._n = n

    def __call__(self, x):
        print("Call")
        return self._n * x

double = Multipliyer(2)
print(double(2))


class scale:
    def __init__(self, n):
        self._n = n

    def __call__(self, f):
        def wrapper(x):
            return f(x * self._n)
        return wrapper


@scale(5)
def get_area(x):
    return x * x

print(get_area(5))


class memo:
    def __init__(self):
        self._state = {}

    def __call__(self, f):
        def wrapper(n):
            if n not in self._state:
                self._state[n] = f(n)
            return self._state[n]
        return wrapper


@memo()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(20))

print('=============== magic method __new__ =====================')


class C:
    def __new__(cls):
        return 42

a = C()
print(type(a), a)


class Car:
    def run(self):
        print('Rrrrrr')


class Truck:
    def run(self):
        print('ZHHHHH')


class Vehicle:
    def __new__(cls, type_):
        if type_ == 'Car':
            return Car()
        elif type_ == 'Truck':
            return Truck()
        else:
            raise ValueError('there is no cow level')

vehicles = ['Car', 'Car', 'Truck', 'Car']
Vehicles = [Vehicle(x) for x in vehicles]
print(Vehicles)

for vehicle in Vehicles:
    vehicle.run()

print('=========== pattern Observer ================')


def a():
    print('a')


def b():
    print('b')


def c():
    print('c')

observers = []


class Notifiyer:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            res = f(*args, **kwargs)
            for observer in self.observers:
                observer()
            return res
        return wrapper

notifiyer = Notifiyer()


@notifiyer
def f():
    return 42

print(f())
notifiyer.register(a)
print(f())
notifiyer.register(b)
print(f())
