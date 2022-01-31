import unittest
from unittest.mock import MagicMock, patch
from update_steward.config_loader.config_loader import ConfigLoader


class TestConfigLoader(unittest.TestCase):
    

    def test_create_config_loader_object(self):
        config_parser = ConfigLoader()
        self.assertIsInstance(config_parser, ConfigLoader)

    @patch('update_steward.config_loader.config_loader.ConfigParser.read')
    def test_read_config_file(self,mock_config_file: MagicMock):
        config_text = '''
        [DEFAULT]
        before_reboot = /scripts/before_reboot
        '''
        config_parser = ConfigLoader()
        config_parser.read_config_file(config_text)
        mock_config_file.assert_called_once()