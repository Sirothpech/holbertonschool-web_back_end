#!/usr/bin/env python3
"""Test client
"""
import unittest
from unittest.mock import PropertyMock, patch
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

    def test_public_repos_url(self):
        """Test the _public_repos_url
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:

            mock_org.return_value = {"https://example.com"}
            github_client = GithubOrgClient("example")
            result = github_client.org
            self.assertEqual(result, {"https://example.com"})

    def test_public_repos(self):
        """Test the _public_repos method
        """
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_org:

            mock_org.return_value = {"https://example.com"}
            with patch("client.get_json") as mock_get_json:
                mock_get_json.return_value = [{"name": "example"}]
                github_client = GithubOrgClient("example")
                result = github_client.public_repos()
                self.assertEqual(result, ["example"])
                mock_get_json.assert_called_once_with("https://example.com")
