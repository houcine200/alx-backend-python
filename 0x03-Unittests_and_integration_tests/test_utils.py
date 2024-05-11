#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Dict, Tuple, Any
from unittest.mock import patch, Mock
from utils import get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, nested_map: Dict[str, Any], path: Tuple[str], expected: Any
    ) -> None:
        """test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(
        self, nested_map: Dict[str, Any], path: Tuple[str]
    ) -> None:
        """test access_nested_map function for exceptions"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Defines a test case class for testing the 'get_json' function"""
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ test that utils.get_json returns the expected result. """
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """to mock a_method. Test that when calling a_property twice,
    """

    def test_memoize(self):
        """to mock a_method. Test that when calling a_property twice"""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                """A memoized property"""
                return self.a_method()

        @patch.object(TestClass, 'a_method')
        def test_memoize(self, mock_a_method):
            """Inner test function to patch a_method and check calls"""
            instance = self.TestClass()

            result1 = instance.a_property()
            result2 = instance.a_property()

            mock_a_method.assert_called_once()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
