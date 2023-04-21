#!/usr/bin/env python3
"""
TestAccessNestedMap class to test access_nested_map function
"""
import unittest
from parameterized import parameterized


access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ test_access_nested_map class """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """ Method to check the function return value """
        test = access_nested_map(nested_map, path)
        self.assertEqual(test, result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Method to check the exception raised """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
