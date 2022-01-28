from enum import Enum, unique, auto
from typing import Any
from logger_system.log_level import LogLevel
import syslog

@unique
class SyslogLevel(LogLevel):

    DEBUG = syslog.LOG_DEBUG
    INFO = syslog.LOG_INFO
    WARNING = syslog.LOG_WARNING
    ERROR = syslog.LOG_ERR
    CRITICAL = syslog.LOG_CRIT
