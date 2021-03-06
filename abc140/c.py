import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3
2 5"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
3"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
0 153 10 10 23"""
        output = """53"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


def resolve():
    n = int(input())
    b = list(map(int, input().split()))
    a = []
    a.append(b[0])
    for i in range(n-2):
        a.append(min(b[i], b[i+1]))
    a.append(b[n-2])
    print(sum(a))
