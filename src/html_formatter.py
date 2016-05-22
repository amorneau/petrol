import markdown2

class HtmlFormatter:
    _TEMPLATE = '''<html>
<head>
<title></title>
</head>
<body>
{}
</body>
</html>'''

    def get_html(self, post):
        html_body = markdown2.markdown(post.content)
        return self._TEMPLATE.format(html_body)
