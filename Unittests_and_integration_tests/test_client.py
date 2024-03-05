#!/usr/bin/env python3
"""Test client module
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org):
        """Test the org method
        """
        with patch('client.get_json') as mock_get_json:
            mock_get_json.return_value = {}

            github_client = GithubOrgClient(org)
            result = github_client.org
            mock_get_json.assert_called_once()
            self.assertEqual(result, {})

    def test_public_repos_url(self):
        """Test the _public_repos_url property
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:

            mock_org.return_value = {"https://example.com"}
            github_client = GithubOrgClient("example")
            result = github_client.org
            self.assertEqual(result, "https://example.com")

    def test_public_repos(self):
        """Test the public_repos method
        """
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_org:

            mock_org.return_value = "https://example.com"
            with patch("client.get_json") as mock_get_json:
                mock_get_json.return_value = [{"name": "example"}]
                github_client = GithubOrgClient("example")
                result = github_client.public_repos()
                self.assertEqual(result, ["example"])
                mock_get_json.assert_called_once_with("https://example.com")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method
        """
        github_client = GithubOrgClient("example")
        result = github_client.has_license(repo, license_key)
        self.assertEqual(result, expected)
