import context

from html_formatter import HtmlFormatter
from post import Post
from writer import Writer

import os
from unittest import TestCase

class WriterTests(TestCase):
    def setUp(self):
        self._post = self._make_post()
        self._writer = self._make_writer()

    def tearDown(self):
        for current_file in os.listdir():
            if '.html' in current_file:
                os.remove(current_file)

    def test_duplicate_post(self):
        self._writer.write_post(self._post)

        with self.assertRaises(ValueError):
            self._writer.write_post(self._post)

    def test_successful_write(self):
        self._writer.write_post(self._post)

        for current_file in os.listdir():
            if '.html' in current_file:
                html_file = open(current_file, 'r')
                html_content = html_file.read()

                self.assertTrue(self._post.content in html_content)

    def _make_post(self):
        file_name = 'dummy.md'
        file_content = 'Dummy content'

        return Post(file_name, file_content)

    def _make_writer(self):
        template = '<html><head></head><body>{}</body></html>'
        return Writer(template)
