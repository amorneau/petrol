import context

from html_formatter import HtmlFormatter
from post import Post

from unittest import TestCase

class HtmlFormatterTests(TestCase):
    def setUp(self):
        self._formatter = HtmlFormatter()

    def test_title_formatting(self):
        title = 'Title'
        content = '## {}'.format(title)

        post = Post('dummy.md', content)
        html = self._formatter.get_html(post)

        self.assertTrue('<h2>{}</h2>'.format(title) in html)

    def test_date_formatting(self):
        date = 'May 23, 2016'
        content = '_{}_'.format(date)

        post = Post('dummy.md', content)
        html = self._formatter.get_html(post)

        self.assertTrue('<em>{}</em>'.format(date) in html)

    def test_multiple_paragraphs(self):
        paragraph1 = 'First paragraph'
        paragraph2 = 'Second paragraph'
        content = '{}\n\n{}'.format(paragraph1, paragraph2)

        post = Post('dummy.md', content)
        html = self._formatter.get_html(post)

        self.assertTrue('<p>{}</p>'.format(paragraph1) in html)
        self.assertTrue('<p>{}</p>'.format(paragraph2) in html)
