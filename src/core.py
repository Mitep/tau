import os


audio_types = ["mp3", "flac", "aac"]
image_types = ["jpg", "jpeg", "png"]
repr_types = ["yaml", "xml", "json"]


class Node:

    all_children = []
    repr_type = "yaml"

    def __init__(self, path):
        self.my_children = []
        if os.path.isdir(path):
            child_dir = self.init_dir(path)
            self.add_child(child_dir)
        else:
            child_file = self.init_file(path)
            self.add_child(child_file)

    def init_file(self, path):
        filename, ext = path.rsplit(".", 1)
        if ext in audio_types:
            audio = AudioFile(path)
            self.add_child(audio)

    def init_dir(self, path):
        self.path = path
        print(path)
        # get all children
        # call Node constructor for all children
        # add children

    def add_child(self, child):
        self.my_children.append(child)
        self.all_children.append(child)

    def __str__(self):
        if self.repr_type == "yaml":
            return (
                "directory:"
                f"path:{self.path}"
            )


class AudioFile(Node):

    def __init__(self, path):
        self.path = path
        self.meta = {}
        # add data to meta dict

    def __str__(self):
        if self.repr_type == "yaml":
            return f"{self.path}"


class ImageFile(Node):

    def __init__(self, path):
        self.path = path
        self.meta = {}
        # add data to meta dict

    def __str__(self):
        if self.repr_type == "yaml":
            return f"{self.path}"
