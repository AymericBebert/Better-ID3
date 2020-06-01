import logging
import os
import re
from typing import List, Dict, Set


class CleanBlacklist:

    logger = logging.getLogger(__name__)

    def apply(self, files_by_directory: Dict[str, List[str]], blacklist: str):
        re_bl = re.compile(blacklist)
        for d, files in files_by_directory.items():
            for f in files:
                if re_bl.match(os.path.basename(f)):
                    self.logger.warning(f"CleanBlacklist: '{f}'")
                    os.unlink(f)
