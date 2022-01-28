from logger_system.logger import Logger
from logger_system.syslog_level import SyslogLevel
import syslog

class SyslogLogger(Logger):

    def write_to_log(self, level: SyslogLevel, message: str):
        syslog.syslog(level, message)