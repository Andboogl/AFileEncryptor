"""Folder decryption module"""


import os


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
                with open(path, 'a') as file:
                    file.write(value)

            except Exception:
                with open(path, 'ab') as file:
                    file.write(value)

        # If it's folder
        elif isinstance(value, dict):
            path = key if not cr else os.path.join(cr, key)

            os.mkdir(path)
            decrypt(data[key], cr=path)

    return cr
