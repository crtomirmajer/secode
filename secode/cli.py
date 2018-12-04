import argparse

from secode.core import encode_secrets

PARSER = argparse.ArgumentParser()
PARSER.add_argument(
    'file_path',
    metavar='file_path',
    help='yaml file with K8S secrets'
)
PARSER.add_argument(
    '-d', '--decode',
    action='store_true',
    help='decode secrets'
)


def run():
    args = PARSER.parse_args()
    content = encode_secrets(args.file_path, args.decode)
    print(content, end='')
