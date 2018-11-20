"""
Classes in this module is used for easy printing states
"""


class AudioFile:
    """
    Represents any audio file
    """
    
    def __init__(self, path):
        self.path = path

    def add(self, key, value):
        self.key = value

    def remove(self, key):
        delattr(self, key)