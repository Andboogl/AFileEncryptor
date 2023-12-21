"""Module to load translation file"""


import json


def load_translation():
    """Load translation file"""
    with open('design/translation/translation.json', 'r') as trf:
        return json.load(trf)
