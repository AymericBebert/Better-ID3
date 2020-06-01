import glob
import logging
import os
from typing import List

import attr

from better_id3.clean import CleanBlacklist, CleanCover


@attr.s(auto_attribs=True)
class CleanCommand:
    directory: str = None
    blacklist: str = None
    cover: List[str] = attr.Factory(list)

    logger = logging.getLogger(__name__)

    def run(self):
        if self.directory is None:
            logging.error("You must specify a directory")
            return
        logging.info(f"Cleaning directory '{self.directory}'")
        logging.info(f"Cleaning directory '{os.path.join(self.directory, '**', '*.mp3')}'")
        files_mp3 = sorted(glob.glob(os.path.join(self.directory, "**", "*.mp3"), recursive=True))
        directories = sorted({os.path.dirname(f) for f in files_mp3})
        all_files = {d: sorted(f for f in glob.glob(os.path.join(d, "*")) if os.path.isfile(f)) for d in directories}
        total_files = sum(len(d) for d in all_files.values())
        logging.info(f"{len(files_mp3)} mp3 files among {total_files} files, in {len(directories)} directories")

        blc = CleanBlacklist()
        blc.apply(all_files, self.blacklist)

        cvc = CleanCover()
        cvc.apply(all_files, set(self.cover))
