from update_steward.logger_system.log_level import LogLevel
from update_steward.logger_system.logger import Logger
import syslog

class SyslogLogger(Logger):

    def write_to_log(self, level: LogLevel, message: str):
        syslog.syslog(level, message)