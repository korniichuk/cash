# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from os.path import dirname, join
from sys import argv, exit

from configobj import ConfigObj

module_location = dirname(__file__)
config_rich_abs_path = join(module_location, "config/rich.ini")
config = ConfigObj(config_rich_abs_path)

argparse = {} # Strings for -h --help
messages = {} # Strings for output


def create_dictionaries():
    """Create "argparse" and "messages" dictionaries"""

    config_argparse_rel_path = config["config_argparse_rel_path"]
    config_argparse_abs_path = join(module_location, config_argparse_rel_path)
    config_messages_rel_path = config["config_messages_rel_path"]
    config_messages_abs_path = join(module_location, config_messages_rel_path)
    with open(config_argparse_abs_path, 'r') as f:
        argparse_list = f.read().splitlines()
    for i in range(0, len(argparse_list), 2):
        argparse[argparse_list[i]] = argparse_list[i+1]
    with open(config_messages_abs_path, 'r') as f:
        messages_list = f.read().splitlines()
    for i in range(0, len(messages_list), 2):
        messages[messages_list[i]] = messages_list[i+1]

def init(args):
    """Init the rich utility"""

    pass

def main():
    """Main function"""

    create_dictionaries()
    args = parse_command_line_args()
    args.function_name(args)

def parse_command_line_args():
    """Parse command line arguments"""

    # Create top parser
    parser = ArgumentParser(prog="rich", description=argparse["_parser"],
                            add_help=True)
    parser.add_argument("-v", "--version", action="version",
                        version="rich 0.1a1")
    # Create subparsers for the top parser
    subparsers = parser.add_subparsers(title=argparse["_subparsers"])
    # Create the parser for the "init" subcommand
    parser_install = subparsers.add_parser("init",
            description=argparse["_parser_init"],
            help=argparse["_parser_init"])
    parser_install.set_defaults(function_name=init)
    if len(argv) == 1:
        parser.print_help()
        exit(0) # Clean exit without any errors/problems
    return parser.parse_args()
