"""Folder decryption module"""


import os


def __create_folder(name):
    """Create folder if it is not exists"""
    if not os.path.exists(name):
        os.mkdir(name)


def decrypt(data: dict, cr=None):
    """Decrypt folder

    Args:
        data (dict): encrypted folder
        cr (str, None): do not set this value
    """
    for key, value in data.items():
        # If it's file
        if isinstance(value, str) or isinstance(value, bytes):
            path = key if not cr else os.path.join(cr, key)

            try:
                with open(path, 'a' if not os.path.exists(path) else 'w') as file:
                    file.write(value)

            except Exception:
                with open(path, 'ab' if not os.path.exists(path) else 'wb') as file:
                    file.write(value)

        # If it's folder
        elif isinstance(value, dict):
            path = key if not cr else os.path.join(cr, key)

            __create_folder(path)
            decrypt(data[key], cr=path)

    return cr
