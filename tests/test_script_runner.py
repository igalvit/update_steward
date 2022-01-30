from unittest.mock import patch
import update_steward.script_runner.script_runner as SR
import unittest
from subprocess import CompletedProcess

path_to_read='./scripts'

class TestScriptRunner(unittest.TestCase):
    @patch('update_steward.script_runner.script_runner.listdir')
    def test_read_folder(self,mock_listdir):
        mock_listdir.return_value = ['file1.sh', 'file2.sh']
        sr = SR.ScriptRunner(path_to_read)
        sr.read_list_of_files()
        self.assertEqual(sr.list_of_files, ['file1.sh', 'file2.sh'])

    @patch('update_steward.script_runner.script_runner.listdir')
    def test_read_folder_exception(self, mock_listdir_exception):
        mock_listdir_exception.side_effect = FileNotFoundError
        sr = SR.ScriptRunner(path_to_read)
        sr.read_list_of_files()
        self.assertRaises(FileNotFoundError)
    
    @patch('update_steward.script_runner.script_runner.listdir')
    @patch('update_steward.script_runner.script_runner.CommandRunner.exec_command')
    def test_exec_list_of_files(self, mock_command_runner, mock_listdir):
        mock_listdir.return_value = ['file1.sh', 'file2.sh']
        mock_exec_command_result : CompletedProcess['bytes'] = \
            CompletedProcess(args='file1.sh',returncode=0,stderr=b'',stdout=b'Command executed')
        mock_command_runner.return_value = mock_exec_command_result
        sr = SR.ScriptRunner(path_to_read)
        sr.read_list_of_files()
        sr.exec_list_of_files()
        mock_command_runner.assert_called()

if __name__ == '__main__':
    unittest.main()