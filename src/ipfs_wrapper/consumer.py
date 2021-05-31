from pathlib import Path
from ipfs_wrapper.ipfsClient import ipfsClient

Hash = str  # multibase encoded multihash


def retrieve(hash: Hash, destination: Path):
    client = ipfsClient()
    client.consume(hash,destination)
    # could we have a progress bar here?
    # hash could be a folder with many files or a single file#
    pass
