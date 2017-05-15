class MyList:
    def __init__(self, l=[]):
        self._l = list(l)

    def __repr__(self):
        return repr(self._l)

    def add(self, a):
        self._l.append(a)

    def __len__(self):
        return len(self._l)

    def __bool__(self):
        return bool(self._l)

    def __contains__(self, obj):
        return obj in self._l

    def __setitem__(self, index, value):
        self._l[index] = value

    def __getitem__(self, index):
        # return self._l[index]
        # print(index)
        if isinstance(index, int):
            return self._l[index]
        elif isinstance(index, tuple):
            return [self._l[i] for i in index]
        elif index == ...:
            return self._l.copy()
        else:
            raise IndexError

    def __iter__(self):
        # return MyListIterator(self._l)
        for i in self._l:
            yield i

# class MyListIterator:
#     def __init__(self, l):
#         print('Iter')
#         self._l = l
#         self._i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         print('Next')
#         self._i += 1
#         if self._i == len(self._l) + 1:
#             raise StopIteration
#         return self._l[self._i - 1]


l1 = MyList(range(10))
print(l1)
print(len(l1))
print(bool(MyList([])))
print(1 in l1)
print(l1[2])
print(l1[1, 3, 4, 7])
print(l1[...])

i = iter(l1)
print(i.__next__())
print(next(i))

for i in l1:
    for j in l1:
        print(i, j)

l2 = [x*x for x in range(10)]
print(l2)
l3 = (x*x for x in range(10))
print(l3)

def infinity_list():
    i = 0
    while True:
        yield i
        i += 1
g = infinity_list()

print(g)

for i in infinity_list():
    if i*i > 100:
        break
    print(i, i*i)

import itertools

print(list(itertools.takewhile(lambda x: x < 100, (x * x for x in itertools.count(0)))))

l4 = [0] * 5 + [1] * 2 + [0] * 7

for i, j in itertools.groupby(l4):
    print(i, len(list(j)))


def coroutine(f):
    gen = f()
    next(gen)
    return gen


@coroutine
def f():
    i = yield
    print('f :', i)
    i = yield i + 1
    print('f :', i)
    i = yield i + 1
    print('f :', i)
    i = yield i + 1
    print('f :', i)


def main():
    i = f.send(0)
    print('Main: ', i)
    i = f.send(i + 1)
    print('Main: ', i)
    i = f.send(i + 1)
    print('Main: ', i)

print(main())
