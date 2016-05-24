#!/usr/bin/python3

from configuration import Configuration
from post import Post
from writer import Writer

import argparse
import sys

class Petrol:
    def __init__(self, input_file_names, config_file_name):
        self._input_file_names = input_file_names

        if config_file_name:
            self._config = Configuration(config_file_name)
        else:
            self._config = Configuration()

        with open(self._config.template_file_name, 'r') as template_file:
            self._template = template_file.read()

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
    parser = argparse.ArgumentParser(description='Generate a blog post.')
    parser.add_argument('input_file', nargs='+')
    parser.add_argument('-c', '--config')
    args = parser.parse_args()

    petrol = Petrol(args.input_file, args.config)
    petrol.run()
