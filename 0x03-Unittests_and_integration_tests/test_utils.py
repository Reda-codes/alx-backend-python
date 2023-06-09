#!/usr/bin/env python3
"""
TestAccessNestedMap class to test access_nested_map function
"""
import unittest
from parameterized import parameterized
import requests
from unittest.mock import patch, Mock


access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


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


class TestGetJson(unittest.TestCase):
    """ TestGetJson class """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ test_get_json Method """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ TestMemoize class """
    def test_memoize(self):
        """ test_memoize function """
        class TestClass:

            def a_method(self):
                """ a_method method """
                return 42

            @memoize
            def a_property(self):
                """ a_property method """
                return self.a_method()

        with patch.object(TestClass, "a_method") as mockMethod:
            test = TestClass()
            p1 = test.a_property
            p2 = test.a_property
            mockMethod.assert_called_once
