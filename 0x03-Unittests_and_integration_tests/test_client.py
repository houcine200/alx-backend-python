import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """_class and implement the test_org method.
    """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get: Mock) -> None:
        """ test that GithubOrgClient.org returns the correct value."""
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {"payload": True})
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get.assert_called_once_with(url)
