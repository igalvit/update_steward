from abc import ABC, abstractclassmethod
from logger_system.log_level import LogLevel

class Logger(ABC):

    @abstractclassmethod
    def write_to_log(self, level: LogLevel, message: str):
        pass