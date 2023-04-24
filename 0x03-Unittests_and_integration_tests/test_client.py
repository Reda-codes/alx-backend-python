#!/usr/bin/env python3
"""
TestGithubOrgClient class to test client
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
import client


GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient Class """
    @parameterized.expand([
        ("google"),
        ("abc"),
        ])
    @patch("client.get_json",  return_value={"payload": True})
    def test_org(self, orgName, mock_get):
        """ test_org method """
        client = GithubOrgClient(orgName)
        ret = client.org
        self.assertEqual(ret, mock_get.return_value)
        mock_get.assert_called_once
