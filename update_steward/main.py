from distutils.log import INFO
from os import listdir, path
from update_steward.logger_system.log_level import LogLevel
# from update_steward.package_updater.debian_updater import DebianUpdater, Updater
# from update_steward.script_runner.script_runner import ScriptRunner
# from update_steward.system_restarter.system_restarter import SystemRestarter
from version_checker.version_checker import VersionChecker
from logger_system.syslog_logger import SyslogLogger
from logger_system.syslog_level import SyslogLevel



# system_package_updater = Updater(DebianUpdater)
# system_package_updater.update_system()
# if system_package_updater.needs_restart():
#     before_restart_scripts_runner = ScriptRunner('./before_restart')
#     before_restart_scripts_runner.exec_list_of_files()
#     system_rebooter = SystemRestarter()
#     #system_rebooter.reboot_system()

    
# else:
#     exit(0)


sl = SyslogLogger()

sl.write_to_log(SyslogLevel.INFO, "Starting the program.")
sl.write_to_log(SyslogLevel.INFO, "Checking if system is Linux.")
vc = VersionChecker()
if (vc.is_linux):
    linux_version = vc.search_release_file()
    sl.write_to_log(SyslogLevel.INFO("System is %" % linux_version))
else:
    exit(1)
