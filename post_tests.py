from post import Post

from unittest import TestCase

class PostTests(TestCase):
    TITLE = 'Test Title'
    DATE = 'January 1, 2000'
    BODY = '''First paragraph.

    Second paragraph'''
    CONTENT_BASE = '[TITLE]{}[/TITLE]\n[DATE]{}[/DATE]\n[BODY]{}[/BODY]'

    def test_blank_post(self):
        content = self.CONTENT_BASE.format('', '', '')

        with self.assertRaises(ValueError):
            post = Post(content)

    def test_blank_title(self):
        content = self.CONTENT_BASE.format('', self.DATE, self.BODY)

        with self.assertRaises(ValueError):
            post = Post(content)

    def test_blank_date(self):
        content = self.CONTENT_BASE.format(self.TITLE, '', self.BODY)

        with self.assertRaises(ValueError):
            post = Post(content)

    def test_blank_body(self):
        content = self.CONTENT_BASE.format(self.TITLE, self.DATE, '')

        with self.assertRaises(ValueError):
            post = Post(content)

    def test_good_post(self):
        content = self.CONTENT_BASE.format(
                self.TITLE,
                self.DATE,
                self.BODY)

        post = Post(content)
        formatted_content = post.get_html()

        self.assertTrue(self.TITLE in formatted_content)
        self.assertTrue(self.DATE in formatted_content)
        self.assertTrue(self.BODY in formatted_content)
