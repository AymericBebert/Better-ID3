import logging
import logging.config

import fire
import yaml
from configue import load_config_from_dict


class CLI:
    """Better ID3

        ---------------
        examples:
            $ python -m better_id3 --help
            $ python -m better_id3 clean --directory=/Users/John/Music
    """

    def __init__(self, config_path: str = "config.yml") -> None:
        with open(config_path, encoding="utf-8") as config_file:
            config_dict = yaml.load(config_file, Loader=yaml.FullLoader)
        if "logging" in config_dict:
            logging.config.dictConfig(config_dict["logging"])
        self.config = load_config_from_dict(config_dict)

    def clean(self, **kwargs):
        self._run_command("clean", **kwargs)

    def _run_command(self, command_name: str, **kwargs):
        command = self.config[command_name]
        for k, v in kwargs.items():
            setattr(command, k, v)
        command.run()


if __name__ == "__main__":
    fire.Fire(CLI)
