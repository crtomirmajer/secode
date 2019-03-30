import argparse
import sys

from secode.core import encode_file, encode_stream

PARSER = argparse.ArgumentParser()
PARSER.add_argument(
    'file_path',
    metavar='file_path',
    help='yaml file with K8S secrets',
    nargs='?'
)
PARSER.add_argument(
    '-d', '--decode',
    action='store_true',
    help='decode secrets'
)


def run():
    args = PARSER.parse_args()
    if args.file_path:
        content = encode_file(args.file_path, args.decode)
    else:
        content = encode_stream(sys.stdin, args.decode)
    print(content, end='')
