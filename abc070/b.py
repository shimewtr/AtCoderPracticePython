import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, c, d, = map(int, input().split())
    print(max(min(b, d)-max(a, c), 0))


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
        input = """0 75 25 100"""
        output = """50"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """0 33 66 99"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """10 90 20 80"""
        output = """60"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
