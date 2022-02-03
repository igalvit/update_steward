import unittest
from unittest.mock import MagicMock, patch

from update_steward.logger_system.syslog_level import SyslogLevel
from update_steward.logger_system.syslog_logger import SyslogLogger


class TestSyslogLogger(unittest.TestCase):

    @patch('update_steward.logger_system.syslog_logger.syslog.syslog')
    def test_write_to_log_ok(self, mock_syslog: MagicMock) -> None:
        sl = SyslogLogger()
        sl.write_to_log(SyslogLevel.INFO, "Ready to update.")
        mock_syslog.assert_called()


if __name__ == '__main__':
    unittest.main()
