from .cli import get_args
from . import runner


def main():
    args = get_args()
    if args.command == "add":
        runner.add(args.file_path)
    elif args.command == "get":
        runner.get(args.url, args.path)


if __name__ == "__main__":
    main()
