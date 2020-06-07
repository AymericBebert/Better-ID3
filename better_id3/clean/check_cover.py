import logging
import os
from dataclasses import dataclass, field
from typing import Dict, List

from better_id3.clean.model import CleanItem


@dataclass
class EachDirectoryShouldHaveACover(CleanItem):
    allowed: List[str] = field(default_factory=list)

    logger = logging.getLogger(__name__)

    def apply(self, files_by_directory: Dict[str, List[str]]):
        for d, files in files_by_directory.items():
            base_names = [os.path.basename(f) for f in files]
            for a in self.allowed:
                if a in base_names:
                    break
            else:
                self.logger.warning(d)
                for f in base_names:
                    self.logger.debug(f"file '{f}'")
