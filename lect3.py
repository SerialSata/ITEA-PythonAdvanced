f = open('lect3.txt', 'wt')
f.write('String1\n')
f.write('String2\n')
f.flush()
f.write('Строка1\n')
f.close()
print(f)

f = open('lect3.txt', 'rt')
s = f.read()
print(s)
f.close()

f = open('lect3.txt', 'rt')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

f = open('lect3.txt', 'rt')
print(f.read(5))
print(f.read(5))
print(f.read(5))
f.close()

f = open('lect3.txt', 'rb')
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(f.read(5))
f.close()

f = open('lect3.txt', 'rt')
for line in f:
    print(line)
f.close()

with open('lect3.txt', 'rt') as f:
    for line in f:
        print(line)
print(f.closed)

obj = {'a': [1, 2, 3], True: 2.345}
import pickle
s = pickle.dumps(obj)
print(s)
print(pickle.loads(s))

obj1 = {1: (1, 2, 3), 'a': [1, 2, 3], False: None}
import json
s1 = json.dumps(obj1)
print(s1)
print(json.loads(s1))

import os

os.mkdir('lect3')
os.chdir('lect3')
print(os.getcwd())
f = open('file1.txt', 'wt')
f.close()
import os.path
print(os.path.abspath('file1'))
print(os.path.join('aaa', 'bbb', 'ccc'))
os.remove('file1.txt')
os.chdir('..')
os.rmdir('lect3')

for root, dirs, files in os.walk('/home/sata/PycharmProjects/Python Advanced'):
    print(root, dirs, files)
    if '.idea' in files:
        print('!', root)

import tempfile
f = tempfile.TemporaryFile()
print(f)
f.write(b'Hello')
f.seek(0)
print(f.read())
f.close()

import io
s = io.StringIO()
s.write('Hello')
s.seek(0)
print(s.read())

import fnmatch
for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, '*.py'):
        print(filename)

import fcntl
f = open('lect3.txt', 'rt')
fcntl.lockf(f, fcntl.LOCK_SH)
fcntl.lockf(f, fcntl.LOCK_UN)
f.close()
