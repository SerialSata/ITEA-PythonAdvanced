import test_module
import sys
import pprint
from test_module import a

print(sys.modules)

print(test_module in sys.modules)

a = 20

print(a, test_module.a )

test_module.a = 30

print(a, test_module.a )
print(test_module.f(5))

m1 = 'sys'
m = __import__(m1)
print(m.path)

import sys1

from sys1 import t, u

print(u.y, t.z)