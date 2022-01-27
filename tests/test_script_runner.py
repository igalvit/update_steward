from unittest.mock import patch
import script_runner.script_runner as SR
import unittest

path_to_read='./scripts'

class TestScriptRunner(unittest.TestCase):
    @patch('script_runner.script_runner.listdir')
    def test_read_folder(self,mock_listdir):
        mock_listdir.return_value = ['file1.sh', 'file2.sh']
        sr = SR.ScriptRunner(path_to_read)
        sr.read_list_of_files()
        self.assertEqual(sr.list_of_files, ['file1.sh', 'file2.sh'])

    @patch('script_runner.script_runner.listdir')
    def test_read_folder_exception(self, mock_listdir_exception):
        mock_listdir_exception.side_effect = FileNotFoundError
        sr = SR.ScriptRunner(path_to_read)
        sr.read_list_of_files()
        self.assertRaises(FileNotFoundError)


if __name__ == '__main__':
    unittest.main()