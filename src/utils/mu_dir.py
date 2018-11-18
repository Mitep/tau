"""
Utils for music directory.
"""
import os 


def get_dir_files(music_dir):
    """
    Returns list of files and list of directories in music directory.
    """
    
    mu_files = []
    mu_dirs = []

    for root, dirs, files in os.walk(music_dir, topdown=True):
        for name in files:
            mu_files.append(os.path.join(root, name))
        for name in dirs:
            mu_dirs.append(os.path.join(root, name))

    return mu_files, mu_dirs
