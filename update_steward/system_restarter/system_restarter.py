from update_steward.command_runner.command_runner import CommandRunner


class SystemRestarter():
    def __init__(self) -> None:
        pass

    def reboot_system(self):
        cr = CommandRunner(["shutdown", "-r"])
        cr.exec_command()
