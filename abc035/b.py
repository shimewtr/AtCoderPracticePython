import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    n = int(input())
    l = s.count("L")
    r = s.count("R")
    u = s.count("U")
    d = s.count("D")
    c = s.count("?")
    a = abs(l - r)
    b = abs(u - d)
    if n == 1:
        print(a + b + c)
    else:
        if 0 > a + b - c:
            if (a + b - c) % 2 == 0:
                print(0)
            else:
                print(1)
        else:
            print(a+b-c)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input_1(self):
        print("test_input_1")
        input = """UL?
1"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """UD?
1"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """UUUU?DDR?LLLL
1"""
        output = """7"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """UULL?
2"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
