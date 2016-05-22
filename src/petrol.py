#!/usr/bin/python3

from post import Post
from writer import Writer

import argparse
import sys

class Petrol:
    def __init__(self, input_file_names, template_file_name):
        self._input_file_names = input_file_names
        self._template = open(template_file_name, 'r').read()

    def run(self):
        writer = Writer(self._template)

        for file_name in self._input_file_names:
            self._make_post(writer, file_name)

    def _make_post(self, writer, file_name):
        with open(file_name, 'r') as input_file:
            file_contents = input_file.read()
            post = Post(file_name, file_contents)
            writer.write_post(post)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate blog post.')
    parser.add_argument('input_file', nargs='+')
    parser.add_argument('-t', '--template', required=True)
    args = parser.parse_args()

    petrol = Petrol(args.input_file, args.template)
    petrol.run()
