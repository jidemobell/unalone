import unittest

from src.package_unalone import  example


class FunctionsCare(unittest.TestCase):
    def test_add_one(self):
        expected = 6
        self.assertEqual(example.add_one(5), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)