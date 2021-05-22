from pathlib import Path

Hash = str  # multibase encoded multihash


def retrieve(hash: Hash, destination: Path):
    # could we have a progress bar here?
    # hash could be a folder with many files or a single file#
    pass
