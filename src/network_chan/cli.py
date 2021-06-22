import argparse
from pathlib import Path

CLIArgs = argparse.Namespace


def get_args() -> CLIArgs:
    parser = argparse.ArgumentParser(
        prog="network-chan", description="Network module to share chan files."
    )
    subparsers = parser.add_subparsers(help="Choose an action.", dest="command")
    add_parser = subparsers.add_parser(
        "add", help="Hash files and add them to IPFS to be served."
    )
    get_parser = subparsers.add_parser("get", help="Download folder from IPFS.")
    add_parser.add_argument(
        "file_path",
        help="Path to a 'thread folder' on the filesystem.",
        type=Path,
    )
    get_parser.add_argument(
        "url",
        help="URL of an imageboard thread.",
        type=str,
    )
    get_parser.add_argument(
        "-p",
        "--path",
        help="",
        type=lambda p: Path(p).expanduser().resolve(),
        default="~/chan/"
    )
    args = parser.parse_args()
    return args
