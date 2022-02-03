import unittest
from unittest.mock import PropertyMock, patch

from update_steward.version_checker.version_checker import VersionChecker

class TestVersionChecker(unittest.TestCase):

    @patch('update_steward.version_checker.version_checker.isfile')
    def test_search_release_file_equal(self, mock_isfile):
        mock_isfile.return_value = True
        vc = VersionChecker()
        VersionChecker.list_of_release_files = {'testOS': '/etc/testos_release'}
        result = vc.search_release_file()
        self.assertEqual(result, 'testOS')
    
    @patch('update_steward.version_checker.version_checker.isfile')
    def test_search_release_file_not_equal(self, mock_isfile):
        mock_isfile.return_value = False
        vc = VersionChecker()
        VersionChecker.list_of_release_files = {'testOS': '/etc/testos_release'}
        result = vc.search_release_file()
        self.assertNotEqual(result, 'testOS')

    @patch('update_steward.version_checker.version_checker.system')
    def test_is_linux_true(self, mock_system):
        mock_system.return_value = "Linux"
        vc = VersionChecker()
        result = vc.is_linux()
        self.assertTrue(result)
    
    @patch('update_steward.version_checker.version_checker.system')
    def test_is_linux_false(self, mock_system):
        mock_system.return_value = "Windows"
        vc = VersionChecker()
        result = vc.is_linux()
        self.assertFalse(result)
        