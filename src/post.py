import re

class Post:
    def __init__(self, raw_content):
        self.title = self._parse_tag(raw_content, 'TITLE')
        self.date = self._parse_tag(raw_content, 'DATE')
        self.body = self._parse_tag(raw_content, 'BODY')

        if not self.title:
            raise ValueError('Title cannot be empty')
        if not self.date:
            raise ValueError('Date cannot be empty')
        if not self.body:
            raise ValueError('Body cannot be empty')

    def _parse_tag(self, raw_content, tag):
        tag_re = '.*\[{}\](?P<result>.+)\[/{}\].*'.format(tag, tag)
        pattern = re.compile(tag_re, re.DOTALL)
        match = pattern.match(raw_content)

        if match:
            return match.group('result')

        return None
