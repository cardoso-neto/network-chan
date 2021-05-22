import argparse
from pathlib import Path

CLIArgs = argparse.Namespace


def get_args() -> CLIArgs:
    parser = argparse.ArgumentParser(
        description="Network module to share chan files."
    )
    subparsers = parser.add_subparsers(help='Choose an action.')
    add_parser = subparsers.add_parser("add", help="Hash files and add them to IPFS.")
    get_parser = subparsers.add_parser("get", help="Download files.")
    add_parser.add_argument(
        "file_paths",
        help="Paths to folders or files on the filesystem.",
        type=Path,
        nargs="*",
    )
    get_parser.add_argument(
        "hashes",
        help="IPFS multibase multihashes.",
        type=Path,
        nargs="*",
    )
    args = parser.parse_args()
    return args
