import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    l = [int(input()) for i in range(m)]
    ans = [0] * (n + 1)
    for i in range(len(ans)):
        ans[i] = i
    for i in range(m):
        a = ans.index(l[i])
        ans[0], ans[a] = ans[a], ans[0]
    for i in range(1, n + 1):
        print(ans[i])

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
        input = """5 6
2
3
5
0
1
3"""
        output = """0
5
2
4
1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 5
0
1
1
1
2"""
        output = """0
1
3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 0"""
        output = """1
2
3
4
5"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """10 7
2
8
5
3
3
8
1"""
        output = """8
0
5
4
3
6
7
2
9
10"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """5 7
3
4
3
1
2
2
0"""
        output = """3
1
2
4
5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()