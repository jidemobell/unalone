import unittest

from src.package_unalone import example


def test_add_one():
    expected = 5
    assert example.add_one(5) == expected
