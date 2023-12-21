"""Buttons handling"""


import pickle
import os
from loguru import logger
import modules


class ButtonsHandler:
    """Buttons handler"""
    def __init__(self, main_window, settings):
        self.main_window = main_window
        self.settings = settings

    def encrypt_button(self):
        """Encrypt user folder"""
        try:
            data = modules.load_translation()
            en = data['en']
            ua = data['ua']
            lang = self.main_window.settings.get_language()

            user_folder = self.main_window.design.to_encrypt.text()
            where_to_make_result = self.main_window.design.where_result.text()

            if user_folder.strip():
                try:
                    encrypted = pickle.dumps(modules.encrypt_folder(user_folder))
                    creation_path = os.path.join(os.path.dirname(user_folder), 'encrypted.pc')\
                        if not where_to_make_result\
                        else os.path.join(where_to_make_result, 'encrypted.pc')

                    with open(creation_path, 'ab' if not os.path.exists(creation_path) else 'wb') as file:
                        file.write(encrypted)

                    text = en['encrypted_version'] if lang == 'en' else ua['encrypted_version']
                    self.main_window.message.normal('AFileEncryptor', f'{text} {creation_path}')

                except Exception as error:
                    logger.error('Error while encrypting folder')
                    logger.error(error)
                    title = en['encryption_error_title'] if lang == 'en' else ua['encryption_error_title']
                    text = en['encryption_error_text'] if lang == 'en' else ua[
                        'encryption_error_text']
                    self.main_window.message.error(title, text, error)

            else:
                text = en['empty_err'] if self.settings.get_language() == 'en' else ua['empty_err']
                self.main_window.message.normal(text, text)

        except Exception as error:
            self.main_window.language_error(error)

    def decrypt_file(self):
        """Decrypt file"""
        try:
            data = modules.load_translation()
            en = data['en']
            ua = data['ua']
            lang = self.settings.get_language()

            file = self.main_window.design.to_decrypt.text()
            where_to_decrypt = self.main_window.design.where_result.text()

            if file.strip():
                try:
                    with open(file, 'rb') as f:
                        data = pickle.load(f)

                    if not where_to_decrypt:
                        where_to_decrypt = os.path.dirname(file)

                    decrypted_path = modules.decrypt(data, cr=where_to_decrypt)

                    text = en['decrypted_text'] if lang == 'en' else ua['decrypted_text']
                    self.main_window.message.normal(f'{text} {decrypted_path}', f'{text} {decrypted_path}')

                except Exception as error:
                    logger.error('Error while decrypting file')
                    logger.error(error)
                    text = en['decryption_error'] if lang == 'en' else ua['decryption_error']
                    self.main_window.message.error(text, text, error)

            else:
                text = en['empty_err'] if self.settings.get_language() == 'en' else ua['empty_err']
                self.main_window.message.normal(text, text)

        except Exception as error:
            self.main_window.language_error(error)


    def chose_decrypt_file_path(self):
        """Chose decrypt file path"""
        file = modules.get_file(self.main_window)
        logger.debug(f'Chosed file: {file}')

        if file:
            self.main_window.design.to_decrypt.setText(file)
            logger.success('Succefly got file path!')

    def chose_encrypt_folder_path(self):
        """Chose encrypt folder path"""
        folder = modules.get_folder(self.main_window)
        logger.debug(f'Chosed folder: {folder}')

        if folder:
            self.main_window.design.to_encrypt.setText(folder)
            logger.success('Succefly got result file path!')

    def get_result_path(self):
        """Get result file path"""
        file = modules.get_folder(self.main_window)
        logger.debug(f'Chosed folder: {file}')

        if file:
            self.main_window.design.where_result.setText(file)
            logger.success('Succefly got result folder path!')

    def ukrainian_language(self):
        """Change language to Ukrainian"""
        self.settings.load_language('ua')
        self.main_window.design.setupUi(self.main_window, language=self.settings.get_language())
        self.main_window.buttons_handling()
        self.main_window.show()
        logger.debug('Language setted')

    def english_language(self):
        """Change language to Ukrainian"""
        self.settings.load_language('en')
        self.main_window.design.setupUi(self.main_window, language=self.settings.get_language())
        self.main_window.buttons_handling()
        self.main_window.show()
        logger.debug('Language setted')
