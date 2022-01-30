

from subprocess import CompletedProcess
import unittest
from unittest.mock import patch
from command_runner.command_runner import CommandRunner
from typing import List

class TestCommandRunner(unittest.TestCase):

    def test_command_runner_creation(self) -> None:
        fake_command: List[str] = ['one']
        cr = CommandRunner(fake_command)
        self.assertEqual(cr.command_to_run, fake_command)
        self.assertEqual(cr.return_code, 999)
        self.assertEqual(cr.stderr, '')
        self.assertEqual(cr.stdout, '')

    @patch('command_runner.command_runner.run')
    def test_exec_command(self, mock_subprocess_run):
        fake_command: List[str] = ['two']
        cr = CommandRunner(fake_command)
        mock_result: CompletedProcess['bytes'] = \
            CompletedProcess(args=fake_command,returncode=0,stderr=b'',stdout=b'Command executed')
        mock_subprocess_run.return_value = mock_result
        cr.exec_command()
        self.assertEqual(cr.return_code, mock_result.returncode)
        self.assertEqual(cr.stderr, mock_result.stderr.decode('utf8'))
        self.assertEqual(cr.stdout, mock_result.stdout.decode('utf8'))


if __name__ == '__main__':
    unittest.main()