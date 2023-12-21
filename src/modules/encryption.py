"""Encryption folder module"""


import os


def encrypt_folder(path: str):
    """Encrypt folder

    Args:
        path (str): path to folder 

    Returns:
        dict: encrypted folder
    """
    encrypted = {}

    encrypted[os.path.basename(path)] = {}
    start_path = path
    now_dir = os.path.basename(path)

    for i in os.walk(start_path):
        # Encryption files
        for file in i[2]:
            try:
                with open(os.path.join(i[0]), 'r') as f:
                    data = f.read()

            except (Exception, FileNotFoundError):
                with open(os.path.join(i[0], file), 'rb') as f:
                    data = f.read()

            encrypted[now_dir][file] = data

        # Encryption folders
        for folder in i[1]:
            res = encrypt_folder(os.path.join(start_path, folder))
            encrypted[now_dir].update(res)

        break

    return encrypted
