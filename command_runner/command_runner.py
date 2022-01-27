from asyncio.subprocess import PIPE
from cmath import e
from distutils import command
from distutils.log import error
from subprocess import run, PIPE
from typing import List

class CommandRunner:

    def __init__(self, command_to_run: List[str]):
        self.command_to_run: List[str] = command_to_run
        self.return_code: int = 999
        self.stdout: str = ''
        self.stderr: str = ''
    
    def exec_command(self) -> None:
        result = run(self.command_to_run, capture_output=True)
        self.stdout = result.stdout.decode("utf-8")
        self.stderr = result.stderr.decode("utf-8")
        self.return_code = result.returncode