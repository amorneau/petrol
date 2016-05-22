class HtmlFormatter:
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

    def get_html(self, post):
        return self._TEMPLATE.format(
                post.title,
                post.title,
                post.date,
                post.body)
