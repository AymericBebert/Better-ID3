from dataclasses import dataclass
from typing import Dict, List


@dataclass
class CleanItem:
    read_only: bool = True

    def apply(self, files_by_directory: Dict[str, List[str]]):
        raise NotImplementedError
