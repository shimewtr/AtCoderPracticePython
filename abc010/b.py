import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        target = l[i]
        while (True):
            if target % 2 == 0 or target % 3 == 2:
                ans += 1
                target -= 1
            else:
                break
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

    def test_input1(self):
        print("test_input1")
        input = """3
5 8 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """9
1 2 3 4 5 6 7 8 9"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
