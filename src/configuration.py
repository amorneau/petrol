import json

class Configuration:
    _TEMPLATE_TAG = 'template'

    def __init__(self, file_name='config.json'):
        config_json = self._get_config_json(file_name)
        
        try:
            self.template_file_name = config_json[self._TEMPLATE_TAG]
        except KeyError as error:
            error_message = 'Missing config key. Error: {}'.format(error)
            raise RuntimeError(error_message)

    def _get_config_json(self, file_name):
        with open(file_name, 'r') as config_file:
            contents = config_file.read()
            return json.loads(contents)
