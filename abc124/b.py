import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    highest = l[0]
    ans = 1
    for i in range(1, n):
        if l[i] >= highest:
            ans += 1
            highest = l[i]
    print(ans)


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
        input = """4
6 5 6 8"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5
4 5 3 5 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5
9 5 6 8 4"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
