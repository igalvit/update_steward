from os import listdir, path
from subprocess import CalledProcessError, check_output
from update_steward.command_runner.command_runner import CommandRunner

class ScriptRunner:

    def __init__(self,path_to_read):
        self.path_to_read = path_to_read

    def read_list_of_files(self):
        try:
            self.list_of_files = sorted(listdir(self.path_to_read))
        except FileNotFoundError:
            print('Path not found: ', self.path_to_read)
    
    
    def exec_list_of_files(self):
        for file in self.list_of_files:
            cr = CommandRunner(file)
            cr.exec_command()