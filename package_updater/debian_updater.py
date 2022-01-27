from package_updater.updater import Updater
from command_runner.command_runner import CommandRunner

class DebianUpdater(Updater):
    def update_system(self):
        cr = CommandRunner(["apt", "update"])
        cr.exec_command()
        if cr.return_code != 0:
            print("Error updating. Error code %i. Error message: %s" % (cr.return_code, cr.stderr))

    def needs_restart(self) -> bool:
        cr = CommandRunner(["needrestart", "-r", "i"])
        cr.exec_command()
        if cr.return_code != 0:
            return True
        return False