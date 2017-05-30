import io

word = u'velosiped.com'
with io.open('test.txt', encoding='utf-8') as file:
    for line in file:
        if word in line:
            print(line, end='')
