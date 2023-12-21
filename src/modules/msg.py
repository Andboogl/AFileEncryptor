"""Module to show QMessageBoxes"""


from PyQt6.QtWidgets import QMessageBox


class Message:
    """Messages class"""
    def __init__(self, main_window):
        self.main_window = main_window

    def normal(self, title, text):
        """Show normal message"""
        msg = QMessageBox(self.main_window)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def error(self, title, text, error):
        """Show error type of QMessageBox"""
        msg = QMessageBox(self.main_window)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setDetailedText(str(error))
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.exec()
