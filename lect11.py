import multiprocessing
import time


a = multiprocessing.Value('i', 0)


def f():
    for i in range(10000):
        a.value += 1

q = multiprocessing.Queue()

ps = []

for _ in range(4):
    p = multiprocessing.Process(target=f)
    p.start()
    ps.append(p)

for p in ps:
    p.join()

# print(a.value)

# =========================================================


def double(x):
    if x % 4:
        time.sleep(0.001)
    return x * 2

p = multiprocessing.Pool(4)

# print(p.map(double, range(50)))

# =========================================================

import urllib.request

p1 = multiprocessing.Pool(4)


def get_url(url):
    r = urllib.request.urlopen(url)
    return len(r.read())

# print(p1.map(get_url, ['http://mail.ru'] * 20))

# =========================================================
