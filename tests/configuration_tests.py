import context

from configuration import Configuration

import os
from unittest import TestCase

class ConfigurationTests(TestCase):
    def tearDown(self):
        for current_file in os.listdir():
            if '.json' in current_file:
                os.remove(current_file)

    def test_no_default_file(self):
        with self.assertRaises(FileNotFoundError):
            Configuration()

    def test_no_provided_file(self):
        with self.assertRaises(FileNotFoundError):
            Configuration('no_such_file.json')

    def test_config_without_template(self):
        file_name = 'config.json'
        config_contents = '{}'

        self._write_config_file(file_name, config_contents)

        with self.assertRaises(RuntimeError):
            Configuration()

    def test_default_config_file_name(self):
        file_name = 'config.json'
        config_contents = '{\n\t"template": "template.html"\n}'

        self._write_config_file(file_name, config_contents)

        config = Configuration()

        self.assertEquals(config.template_file_name, 'template.html')

    def test_passed_in_config_file(self):
        file_name = 'katy_perry.json'
        config_contents = '{\n\t"template": "template.html"\n}'

        self._write_config_file(file_name, config_contents)

        config = Configuration(file_name)

        self.assertEquals(config.template_file_name, 'template.html')

    def _write_config_file(self, file_name, contents):
        with open(file_name, 'w') as config_file:
            config_file.write(contents)
