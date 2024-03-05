#!/usr/bin/env python3
"""Test client
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test Github
    """
    @patch('client.get_json')
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    def test_org(self, org):
        """Test org method
        """
        with patch('client.get_json') as mock_get_json:
            mock_get_json.return_value = {}

            github_client = GithubOrgClient(org)
            result = github_client.org
            mock_get_json.assert_called_once()
            self.assertEqual(result, {})
