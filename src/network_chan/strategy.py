from . import cli, runner


def main():
    args = cli.get_args()
    if args.command == "add":
        runner.add(args.file_path)
    elif args.command == "get":
        runner.get(args.url, args.path)
