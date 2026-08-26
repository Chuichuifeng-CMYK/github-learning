import unittest

from hello import greet


class TestGreet(unittest.TestCase):
    def test_name(self):
        self.assertEqual(greet("小明"), "你好，小明！")

    def test_empty_name(self):
        self.assertEqual(greet(""), "你好，学习者！")

    def test_quit(self):
        self.assertEqual(greet("q"), "程序结束。")


if __name__ == "__main__":
    unittest.main()