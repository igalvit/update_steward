import unittest
from unittest.mock import MagicMock, patch
from system_restarter.system_restarter import SystemRestarter
from subprocess import CompletedProcess


class TestSystemRestarter(unittest.TestCase):

    @patch('system_restarter.system_restarter.CommandRunner.exec_command')
    def test_reboot_system(self, mock_command_runner : MagicMock) -> None:
        mock_exec_command_result : CompletedProcess['bytes'] = \
                CompletedProcess(args='shutdown -r',returncode=0,stderr=b'',stdout=b'Command executed')
        mock_command_runner.return_value = mock_exec_command_result
        sys_restart = SystemRestarter()
        sys_restart.reboot_system()
        mock_command_runner.assert_called()
