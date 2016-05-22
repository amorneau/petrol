import markdown2

class HtmlFormatter:
    def get_html(self, post, template):
        html_body = markdown2.markdown(post.content)
        return template.format(html_body)
