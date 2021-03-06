from html_formatter import HtmlFormatter

import os.path

class Writer:
    def __init__(self, template):
        self._template = template

    def write_post(self, post):
        file_name = self._make_file_name(post)

        if self._file_exists(file_name):
            self._existing_file_error(file_name)

        self._write_content(file_name, post)

    def _make_file_name(self, post):
        html_file_name = post.file_name.replace('.md', '.html')
        return html_file_name.lower()

    def _file_exists(self, file_name):
        return os.path.exists(file_name)

    def _existing_file_error(self, file_name):
        raise ValueError('File already exists: {}'.format(file_name))

    def _write_content(self, file_name, post):
        formatter = HtmlFormatter()
        content = formatter.get_html(post, self._template)

        with open(file_name, 'w') as output_file:
            output_file.write(content)
