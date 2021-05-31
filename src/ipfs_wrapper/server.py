from pathlib import Path
from ipfs_wrapper.ipfsClient import ipfsClient

Hash = str  # multibase encoded multihash


def serve(path: Path) -> Hash:
    client = ipfsClient()
    if path.is_dir():
        return client.serveDir(path)
    elif path.is_file():
        return client.serveFile(path)
    else:
        raise ValueError("Bad path.")
