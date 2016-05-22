from html_formatter import HtmlFormatter

import os.path

class Writer:
    def write_post(self, post):
        file_name = self._make_file_name(post)

        if self._file_exists(file_name):
            self._existing_file_error(file_name)

        self._write_content(file_name, post)

    def _make_file_name(self, post):
        title_with_underscores = post.title.replace(' ', '_')
        lower_case_title = title_with_underscores.lower()
        file_name = '{}.html'.format(lower_case_title)

        return file_name

    def _file_exists(self, file_name):
        return os.path.exists(file_name)

    def _existing_file_error(self, file_name):
        raise ValueError('File already exists: {}'.format(file_name))

    def _write_content(self, file_name, post):
        formatter = HtmlFormatter()
        content = formatter.get_html(post)

        with open(file_name, 'w') as output_file:
            output_file.write(content)
