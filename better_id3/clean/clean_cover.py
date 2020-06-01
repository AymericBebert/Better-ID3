import logging
import os
from typing import List, Dict, Set


class CleanCover:

    logger = logging.getLogger(__name__)

    def apply(self, files_by_directory: Dict[str, List[str]], allowed: Set[str]):
        for d, files in files_by_directory.items():
            basenames = [os.path.basename(f) for f in files]
            for a in allowed:
                if a in basenames:
                    break
            else:
                self.logger.warning(f"CleanCover: '{d}'")
                # for f in basenames:
                #     self.logger.info(f"CleanCover: file '{f}'")

