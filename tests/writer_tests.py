import context

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

                self.assertTrue(self._post.title in html_content)
                self.assertTrue(self._post.date in html_content)
                self.assertTrue(self._post.body in html_content)

    def _make_post(self):
        title = 'Test Title'
        date = 'January 1, 2000'
        body = 'First paragraph.\n\nSecond paragraph'

        content_base = '[TITLE]{}[/TITLE]\n[DATE]{}[/DATE]\n[BODY]{}[/BODY]'
        content = content_base.format(title, date, body)

        return Post(content)

    def _make_writer(self):
        return Writer()
