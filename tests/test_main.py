from unittest import TestCase
from unittest.mock import patch

from better_id3.__main__ import CLI


class TestMain(TestCase):
    def setUp(self) -> None:
        self.cli = CLI()
        self.config_path = "config_path"

    def test_format(self):
        self.assert_command_run(self.cli.clean, "clean")

    def assert_command_run(self, cli_fn, command_name):
        with patch("better_id3.__main__.load_config_from_file") as mock_load_config:
            with patch("better_id3.__main__.setup_logging_from_dict") as mock_setup_logging:
                cli_fn(self.config_path)
                mock_load_config.assert_called_with(self.config_path)
                mock_setup_logging.assert_called_with(mock_load_config.return_value["logging"])
                mock_load_config.return_value[command_name].run.assert_called()
