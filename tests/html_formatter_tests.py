import context

from html_formatter import HtmlFormatter
from post import Post

from unittest import TestCase

class HtmlFormatterTests(TestCase):
    def test_html_formatting(self):
        formatter = HtmlFormatter()
        post = self._make_post()

        html = formatter.get_html(post)

        self.assertTrue(post.title in html)
        self.assertTrue(post.date in html)
        self.assertTrue(post.body in html)

    def _make_post(self):
        title = 'Test Title'
        date = 'January 1, 2000'
        body = 'First paragraph.\n\nSecond paragraph'

        content_base = '[TITLE]{}[/TITLE]\n[DATE]{}[/DATE]\n[BODY]{}[/BODY]'
        content = content_base.format(title, date, body)

        return Post(content)
