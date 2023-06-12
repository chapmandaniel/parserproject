import os
import json


class Settings:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "./settings.json")
        self.settings = self.load_settings()

    def load_settings(self):
        with open(self.file_path, 'r') as json_file:
            data = json.load(json_file)
        return data

    def get_setting(self, key):
        return self.settings.get(key, None)

    def set_setting(self, key, value):
        self.settings[key] = value

    def get_start_date(self):
        return self.settings['date_start']

    def get_end_date(self):
        return self.settings['date_end']

    def get_data_path(self):
        return self.settings['data_path']

    def get_file_name(self):
        return self.settings['file_name']


if __name__ == '__main__':
    settings = Settings()
    print(settings.get_setting('data_path'))
    print(settings.get_setting('date_start'))
    print(settings.get_setting('date_end'))
    print(settings.get_setting('delimiter'))
