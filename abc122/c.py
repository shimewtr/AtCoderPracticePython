import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, m = map(int, input().split())
    s = input()
    t = [0] * (n+1)
    for i in range(n):
        if s[i:i + 2] == "AC":
            t[i + 1] = t[i] + 1
        else:
            t[i + 1] = t[i]
    for i in range(m):
        a, b = map(int, input().split())
        print(t[b-1] - t[a-1])


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
        input = """8 3
ACACTACG
3 7
2 3
1 8"""
        output = """2
0
3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
