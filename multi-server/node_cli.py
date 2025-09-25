import argparse
import mmap

def submit_info(args):
    with open(args.filepath, mode="r+", encoding="utf-8") as file_obj:
        file_obj.truncate(100)
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_WRITE, offset=0) as mmap_obj:
            text = "#submit_info"  # Hoàn thiện: Viết command vào file
            mmap_obj.write(text.encode("utf-8"))

def get_list_command(args):
    with open(args.filepath, mode="r+", encoding="utf-8") as file_obj:
        file_obj.truncate(100)
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_WRITE, offset=0) as mmap_obj:
            text = "#get_list"
            mmap_obj.write(text.encode("utf-8"))

class NodeCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(prog="NodeCLI", description="CLI for interacting with Node")
        subparsers = self.parser.add_subparsers()
        # Submit command
        submit_parser = subparsers.add_parser("submit")
        submit_parser.add_argument("--filepath", required=True)
        submit_parser.set_defaults(func=submit_info)
        # Get list command
        getlist_parser = subparsers.add_parser("getlist")
        getlist_parser.add_argument("--filepath", required=True)
        getlist_parser.set_defaults(func=get_list_command)

    def run(self):
        args = self.parser.parse_args()
        args.func(args)

if __name__ == "__main__":
    cli = NodeCLI()
    cli.run()