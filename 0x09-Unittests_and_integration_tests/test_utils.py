#!/usr/bin/env python3
"""Unittest for utils
"""
import unittest
import requests
from unittest import mock
from parameterized import parameterized
from utils import (access_nested_map, get_json, memoize)
from typing import (Tuple, Any, Dict)


class TestAccessNestedMap(unittest.TestCase):
    """Test for utils
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, a: Dict, b: Tuple, out: Any):
        """test cases for access_nested_map method"""
        self.assertEqual(access_nested_map(a, b), out)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)])
    def test_access_nested_map_exception(self, a: Dict, b: Tuple, out: Any):
        """Method to handle and test utils.access_nested_map raises"""
        self.assertRaises(out, access_nested_map, a, b)


class TestGetJson(unittest.TestCase):
    """Class for Test of get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})])
    @mock.patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict,
                      mock_requests: mock.MagicMock):
        """test get_json method
        """
        mock_requests(test_url)
        mock_requests.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Class for Test Memoize"""
    def test_memoize(self):
        """Test memoize method
        """
        class TestClass:
            """Class
            """
            def a_method(self):
                """A method"""
                return 42

            @memoize
            def a_property(self):
                """A property method"""
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as mock_method:
            mock_method()
            mock_method.assert_called_once()
