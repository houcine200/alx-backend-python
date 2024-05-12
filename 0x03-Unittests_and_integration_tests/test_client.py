import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get: Mock) -> None:
        client = GithubOrgClient(org_name)
        client.org()
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get.assert_called_once_with(url)
