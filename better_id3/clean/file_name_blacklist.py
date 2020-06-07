import logging
import os
import re
from dataclasses import dataclass
from typing import Dict, List

from .model import CleanItem


@dataclass
class FileNameBlacklist(CleanItem):
    blacklist: str = 'no_file_should_match_this_regex'

    logger = logging.getLogger(__name__)

    def apply(self, files_by_directory: Dict[str, List[str]]):
        re_bl = re.compile(self.blacklist)
        for d, files in files_by_directory.items():
            for f in files:
                if re_bl.match(os.path.basename(f)):
                    self.logger.warning(f)
                    if not self.read_only:
                        os.unlink(f)
