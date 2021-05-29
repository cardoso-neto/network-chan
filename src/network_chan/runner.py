import shutil
from pathlib import Path

from chan_url_lib import ChanURI

import dht_wrapper as dht
import ipfs_wrapper as ipfs


def add(thread_folder: Path):
    # hash_ = ipfs.serve(path)
    url = str(ChanURI.from_path(thread_folder))
    # dht.put(url, hash_)


def get(url: str, destination_path: Path):
    thread_url = ChanURI.from_url(url)
    standardized_url = str(thread_url)
    # hash_ = dht.get(url)
    # ipfs.get(hash_, destination_path)
    # shutil.move(destination_path / hash_, destination_path / str(thread_url.thread_id))
