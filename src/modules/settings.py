"""Module to work with application settings"""


import os
import json


class ApplicationSettings:
    """Application settings"""
    def __init__(self):
        self.folder_path = os.path.join(os.path.expanduser('~'), '.AFileEncryptor')
        self.file_path = os.path.join(self.folder_path, 'settings.json')

    def get_language(self):
        """Get current application language"""
        if not os.path.exists(self.file_path):
            return 'en'

        else:
            with open(self.file_path) as file:
                return json.load(file)['language']

    def load_language(self, language: str):
        """Load application language to settings file

        Args:
            language (str): language to load
        """
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)

        with open(self.file_path, 'w' if os.path.exists(self.file_path) else 'x') as file:
            json.dump({'language': language}, file)
