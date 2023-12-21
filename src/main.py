"""Main module. Runs the app"""


import os
from sys import argv
from loguru import logger
from PyQt6.QtWidgets import QApplication
from app import MainWindow


# Logger settings
logs_folder_path = os.path.join(os.path.expanduser('~'), '.AFileEncryptor', 'logs')

logger.add(
    sink=os.path.join(logs_folder_path, 'logs.log'),
    rotation='10KB',
    compression='zip'
)


def main():
    """Runs application"""
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
