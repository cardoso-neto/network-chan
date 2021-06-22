from . import cli, runner


def main():
    args = cli.get_args()
    if args.command == "add":
        print(runner.add(args.file_path))
    elif args.command == "get":
        print(runner.get(args.url, args.path))
