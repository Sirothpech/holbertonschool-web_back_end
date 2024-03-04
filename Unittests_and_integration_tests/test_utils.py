#!/usr/bin/env python3
"""Unittests
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test the access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test the access_nested_map function
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Test get json function
    """
    @parameterized.expand([
        ("http://example.com"),
        ("http://holberton.io")
    ])
    def test_get_json(self, url):
        """ Test get json
        """
        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = {"payload": True}
            self.assertEqual(get_json(url), {"payload": True})


class TestMemoize(unittest.TestCase):
    """ Test memoize function
    """
    def test_memoize(self):
        """ Test memoize function
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        my_obj = TestClass()
        with patch.object(my_obj, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42
            result = my_obj.a_property
            self.assertEqual(result, 42)
            result = my_obj.a_property
            mock_a_method.assert_called_once()
