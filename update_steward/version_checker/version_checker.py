from os.path import isfile
from platform import system

class VersionChecker:

    list_of_release_files:str = {
        "CentOS":"/etc/centos-release",
        "RHEL":"/etc/redhat-release",
        "SuSE":"/etc/SuSE-release",
        "Fedora":"/etc/fedora-release",
        "Oracle":"/etc/oracle-release",
        "Debian":"etc/debian_version",
        "Ubuntu":"/etc/lsb-release",
    }
    unknown_distro: str = "Unknown"

    def search_release_file(self)->str:
        """
            Tries to detect the operating system search release file in /etc.
        """
        for os_name, file_path in VersionChecker.list_of_release_files.items():
            if isfile(file_path):
                return os_name
        return VersionChecker.unknown_distro
    
    def is_linux(self)->bool:
        """
            Checks if operating system is either Linux or other type.
        """
        if system() == 'Linux':
            return True
        return False
