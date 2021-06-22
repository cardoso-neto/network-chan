from pathlib import Path

from chan_url_lib import ChanURI

import dht_wrapper as dht
import ipfs_wrapper as ipfs


def add(thread_folder: Path):
    hash_ = ipfs.serve(thread_folder)
    url = str(ChanURI.from_path(thread_folder))
    # dht.put(url, hash_)
    return hash_


def get(url: str, destination_path: Path) -> Path:
    thread_url = ChanURI.from_url(url)
    # hash_ = dht.get(str(thread_url))
    thread_folder_path = destination_path / thread_url
    ipfs.retrieve(hash_, thread_folder_path)
    return thread_folder_path
