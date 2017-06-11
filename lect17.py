import csv


# @profile
def load():
    res = []
    with open('Pokemon.csv', 'rt') as f:
        r = csv.reader(f)
        next(r, None)
        for row in r:
            res.append(row)
    return res


# @profile
def max_total(r):
    m = 0
    for row in r:
        if m < int(row[4]):
            m = int(row[4])
    return m

if __name__ == '__main__':
    print(max_total(load()))
