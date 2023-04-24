#!/usr/bin/env python3
"""
TestGithubOrgClient class to test client
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """ test_public_repos_url method """
        with patch.object(GithubOrgClient,
                          "org", new_callable=PropertyMock,
                          return_value={"repos_url": "testing"}
                          ) as mockMethod:
            test = GithubOrgClient({"repos_url": "testing"}
                                   .get("repos_url"))
            ret = test._public_repos_url
            mockMethod.assert_called_once
            self.assertEqual(ret, mockMethod.return_value.get("repos_url"))
