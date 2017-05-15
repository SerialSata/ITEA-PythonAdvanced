class MyList(list):
    def sum(self):
        s = 0
        for i in self:
            s += i
        return s

l = MyList([1, 2, 3, 4])

print(dir(l))
print(l.sum())

