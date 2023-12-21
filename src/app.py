"""One of main module. Handling graphical interface"""


import pickle
import os
import modules
from loguru import logger
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from design.design import Ui_MainWindow
from buttons_handling import ButtonsHandler


class MainWindow(QMainWindow):
    """Main window"""
    def __init__(self):
        QMainWindow.__init__(self)

        # Application utils
        self.message = modules.Message(self)

        self.settings = modules.ApplicationSettings()
        self.buttons_handler = ButtonsHandler(self, self.settings)

        # Loading design
        self.design = Ui_MainWindow()

        try:
            lang = self.settings.get_language()

            if lang == 'ua' or lang == 'en':
                self.design.setupUi(self, language=lang)

            else:
                raise Exception(f'Language {lang} is not defind')

        except Exception as error:
            self.language_error(error)

        self.buttons_handling()
        logger.success('Application started its work!')

    def language_error(self, error):
        """Loading language error"""
        logger.error(f'Error while loading application language')
        logger.error(error)
        self.message.error(
            'Error',
            f'Something went wrong while application was loading\'its language. Delete file on path {self.settings.file_path}',
            error)
        self.design.setupUi(self, language='en')

    def buttons_handling(self):
        """Handling buttons click"""
        # Window button
        self.design.close.clicked.connect(exit)
        self.design.roll_up.clicked.connect(self.showMinimized)

        # Menu bar buttons
        self.design.english_language.triggered.connect(self.buttons_handler.english_language)
        self.design.ukrainian_language.triggered.connect(self.buttons_handler.ukrainian_language)

        # Application buttons (Main button)
        self.design.chose_where_result.clicked.connect(self.buttons_handler.get_result_path)
        self.design.chose_to_encrypt.clicked.connect(self.buttons_handler.chose_encrypt_folder_path)
        self.design.chose_to_decrypt.clicked.connect(self.buttons_handler.chose_decrypt_file_path)
        self.design.encrypt.clicked.connect(self.buttons_handler.encrypt_button)
        self.design.set_default.clicked.connect(lambda: self.design.where_result.setText(''))
        self.design.decrypt.clicked.connect(self.buttons_handler.decrypt_file)

    # Moving frameless window
    # --------------------------
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.initial_pos = event.position().toPoint()
        super().mousePressEvent(event)
        event.accept()

    def mouseMoveEvent(self, event):
        if self.initial_pos is not None:
            delta = event.position().toPoint() - self.initial_pos
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
            self.window().move(
                self.window().x() + delta.x(),
                self.window().y() + delta.y(),
            )
        super().mouseMoveEvent(event)
        event.accept()

    def mouseReleaseEvent(self, event):
        self.initial_pos = None
        self.setCursor(Qt.CursorShape.ArrowCursor)
        super().mouseReleaseEvent(event)
        event.accept()
        logger.success('Succefly moved window!')
    # --------------------------
