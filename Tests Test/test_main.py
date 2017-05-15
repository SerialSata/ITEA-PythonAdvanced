import unittest
import unittest.mock
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        self.m = main.Maxer([1, 2, 3])
        print('SetUp')

    @unittest.mock.patch('main.f')
    def testMax1(self, a):
        print(a)
        a.side_effect = [0]
        self.assertEqual(self.m.max(), 3, 'max(1, 2, 3) broken')

    def testMax2(self):
        self.m.append(5)
        self.assertEqual(self.m.max(), 5)

    def tearDown(self):
        print('TearDown')
