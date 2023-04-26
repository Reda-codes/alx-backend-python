#!/usr/bin/env python3
"""
TestGithubOrgClient class to test client
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
import client
from urllib.error import HTTPError
from fixtures import TEST_PAYLOAD


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

    @patch("client.get_json",  return_value=[{"name": "testing"}])
    def test_public_repos(self, mock_get):
        """ test_public_repos method """
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://testing.com/"
                          ) as mock_pub:
            test = GithubOrgClient("testing")
            ret = test.public_repos()
            self.assertEqual(ret, ["testing"])
            mock_get.assert_called_once
            mock_pub.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, license_key, expected_return):
        """ test_has_license method """
        test = GithubOrgClient("testing")
        ret = test.has_license(repo, license_key)
        self.assertEqual(expected_return, ret)


@parameterized_class((
    "org_payload",
    "repos_payload",
    "expected_repos",
    "apache2_repos"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(clss):
        """ setUpClass method """
        clss.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClass(clss):
        """ tearDownClass method """
        clss.get_patcher.stop()

    def test_public_repos(self):
        """ test_public_repos method """
        pass        

    def test_public_repos_with_license(self):
        """ test_public_repos_with_license method """
        pass
