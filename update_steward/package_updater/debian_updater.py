from update_steward.command_runner.command_runner import CommandRunner
from update_steward.package_updater.updater import Updater


class DebianUpdater(Updater):
    def update_system(self) -> None:
        cr = CommandRunner(["apt", "update"])
        cr.exec_command()
        if cr.return_code != 0:
            print("Error updating. Error code %i. Error message: %s" %
                  (cr.return_code, cr.stderr))

    def needs_restart(self) -> bool:
        cr = CommandRunner(["needrestart", "-r", "i"])
        cr.exec_command()
        if cr.return_code != 0:
            return True
        return False
