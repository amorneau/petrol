import re

class Post:
    _TEMPLATE = '''<html>
  <head>
    <title>{}</title>
  </head>
  <body>
    <h2>{}</h2>
    <p><em>{}</em></p>
    <p>{}</p>
  </body>
</html>
    '''

    def __init__(self, raw_content):
        self._title = self._parse_tag(raw_content, 'TITLE')
        self._date = self._parse_tag(raw_content, 'DATE')
        self._body = self._parse_tag(raw_content, 'BODY')

        if not self._title:
            raise ValueError('Title cannot be empty')
        if not self._date:
            raise ValueError('Date cannot be empty')
        if not self._body:
            raise ValueError('Body cannot be empty')

    def get_html(self):
        return self._TEMPLATE.format(
                self._title,
                self._title,
                self._date,
                self._body)

    def _parse_tag(self, raw_content, tag):
        tag_re = '.*\[{}\](?P<result>.+)\[/{}\].*'.format(tag, tag)
        pattern = re.compile(tag_re, re.DOTALL)
        match = pattern.match(raw_content)

        if match:
            return match.group('result')

        return None
