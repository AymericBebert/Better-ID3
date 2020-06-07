import glob
import logging
import os
from dataclasses import dataclass, field
from typing import List

from better_id3.clean.model import CleanItem


@dataclass
class CleanCommand:
    directory: str
    clean_items: List[CleanItem] = field(default_factory=list)

    logger = logging.getLogger(__name__)

    def run(self):
        self.logger.info(f"Cleaning directory '{self.directory}'")
        files_mp3 = sorted(glob.glob(os.path.join(self.directory, "**", "*.mp3"), recursive=True))
        directories = sorted({os.path.dirname(f) for f in files_mp3})
        all_files = {d: sorted(f for f in glob.glob(os.path.join(d, "*")) if os.path.isfile(f)) for d in directories}
        total_files = sum(len(d) for d in all_files.values())
        self.logger.info(f"{len(files_mp3)} mp3 files among {total_files} files, in {len(directories)} directories")

        for item in self.clean_items:
            item.apply(all_files)
