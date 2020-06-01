import logging

import fire
from configue import load_config_from_file
from illuin_logging import setup_logging_from_dict

LOGGER = logging.getLogger(__name__)


class CLI:
    """Better ID3

        ---------------
        examples:
            >>> python -m better_id3 --help
    """

    def clean(self, config_path: str, **kwargs):
        self._run_command(config_path, "clean", **kwargs)

    @staticmethod
    def _run_command(config_path: str, command_name: str, **kwargs):
        config = load_config_from_file(config_path)
        setup_logging_from_dict(config["logging"])
        command = config[command_name]
        for k, v in kwargs.items():
            setattr(command, k, v)
        command.run()


if __name__ == "__main__":
    # starting the Command Line Interface
    LOGGER.info(f"starting {CLI.__name__}")
    fire.Fire(CLI)
