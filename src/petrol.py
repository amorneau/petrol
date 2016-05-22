#!/usr/bin/python3

from post import Post
from writer import Writer

import sys

def print_usage():
    usage_message = 'petrol <input_file1> [<input_file2> ...]'
    print(usage_message)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print_usage()
        sys.exit(1)

    writer = Writer()

    for file_name in sys.argv[1:]:
        with open(file_name, 'r') as input_file:
            file_contents = input_file.read()

            post = Post(file_name, file_contents)
            writer.write_post(post)
