# import random
#
# class Pool:
#     def __init__(self, w, l, b_f, s_f):
#         self._w, self._l = w, l
#         self._fishes = self._create_fishes(BigFish, b_f) + \
#                        self._create_fishes(SmallFish, s_f)
#
#
#     def _create_fishes(self, cls, qty):
#         return [cls(
#             random.randint(1, self._w),
#             random.randint(1, self._l),
#             self
#         ) for _ in range(qty)]
#
#     def move_fishes(self):
#         for fish in self._fishes:
#             fish.move()
#
#
#     def __repr__(self):
#         return '\n'.join([str(fish) for fish in self._fishes])
#
#
# class Fish:
#     def __init__(self, x, y, pool):
#         self._x, self._y = x, y
#         self._pool = pool
#
#     def __repr__(self):
#         return "{}(x={}, y={})".format(
#             self.__class__.__name__,
#             self._x,
#             self._y
#         )
#
#
# class SmallFish(Fish):
#     def __init__(self, x, y, pool):
#         super().__init__(x, y, pool)
#
#     def move(self):
#         self._x = self._x + random.randint(-1, 1)
#         self._y = self._y + random.randint(-1, 1)
#         self._x = 1 if self._x < 1 else self._x
#
#
# class BigFish(Fish):
#     def __init__(self, x, y, pool):
#         super().__init__(x, y, pool)
#
#     def move(self):
#         self._x = self._x + random.randint(-1, 1)
#         self._y = self._y + random.randint(-1, 1)
#
#
# if __name__ == "__main__":
#     p = Pool(10, 10, 3, 5)
#     print(p)


class A:
    def __init__(self):
        self.x = 1

    def __setattr__(self, name, value):
        if name == 'x' and hasattr(self, name):
            raise AttributeError('x is read-only')
        super().__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'x':
            raise AttributeError('x is read-only')
        super().__delattr__(name)

a = A()
a.y = 8
# a.x = 2
print(vars(a))


class B:
    def m1(self):
        print(B.m1)

    def m2(self):
        print(B.m2)


class Proxy:
    def __init__(self):
        self.a = B()

    def m1(self):
        print('Proxy.m1')

    def __getattr__(self, name):
        return getattr(self.a, name)

p = Proxy()
print(p.m1())
print(p.m2())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Person({}, {})'.format(self.name, self.age)

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash(self.name)

    def __lt__(self, other):
        return self.name < other.name


p = Person('Bill', 32)
p1 = Person('Bill', 32)
print(p == p1)
print(p == 1)

l = [Person('Bob', 23), Person('Bill', 32), Person('John', 32)]
print(l.index(Person('Bill', 32)))

s = {Person('Bill', 23), Person('John', 34), Person('Bill', 23)}
print(s)

l1 = [Person('Bill', 23), Person('John', 34), Person('Bill', 34)]
print(l1.sort())
