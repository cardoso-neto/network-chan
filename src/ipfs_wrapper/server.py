from pathlib import Path

Hash = str  # multibase encoded multihash


def serve(path: Path) -> Hash:
    if path.is_dir():
        pass
    elif path.is_file():
        pass
    else:
        raise ValueError("Bad path.")
