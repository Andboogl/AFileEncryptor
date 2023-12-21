"""Module to get user file"""


import os
from PyQt6.QtWidgets import QFileDialog


def get_file(main_window):
    """Get user file"""
    file = QFileDialog.getOpenFileName(main_window,
                                       'AFileEncryptor',
                                       os.path.expanduser('~'))[0]
    return file


def get_folder(main_window):
    """Get user folder path"""
    folder = QFileDialog.getExistingDirectory(main_window, 'AFileEncryptor', os.path.expanduser('~'))
    return folder
