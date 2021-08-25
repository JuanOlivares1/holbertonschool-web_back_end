#!/usr/bin/env python3
"""Unittest for utils
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import (
    Tuple,
    Any,
    Dict
)


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
