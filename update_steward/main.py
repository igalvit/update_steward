from os import listdir, path
from update_steward.package_updater.debian_updater import DebianUpdater, Updater
from update_steward.script_runner.script_runner import ScriptRunner
from update_steward.system_restarter.system_restarter import SystemRestarter

# system_package_updater = Updater(DebianUpdater)
# system_package_updater.update_system()
# if system_package_updater.needs_restart():
#     before_restart_scripts_runner = ScriptRunner('./before_restart')
#     before_restart_scripts_runner.exec_list_of_files()
#     system_rebooter = SystemRestarter()
#     #system_rebooter.reboot_system()

    
# else:
#     exit(0)


