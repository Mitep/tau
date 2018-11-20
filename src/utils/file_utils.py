"""
Utils for working with files and directories.
"""
import os 


def get_dirs(root_dir, recursive=True):
    """
    Return all directories for given path
    """
    ret_dirs = []
    
    for root, dirs, files in os.walk(root_dir, topdown=True):
        
        for name in dirs:
            ret_dirs.append(os.path.join(root, name))
        
        if not recursive:
            break

    return ret_dirs


def get_files(root_dir, recursive=True):
    """
    Return all files for given directory
    """
        
    ret_files = []

    for root, dirs, files in os.walk(root_dir, topdown=True):

        for name in files:
            ret_files.append(os.path.join(root, name))
        
        if not recursive:
            break
        
    return ret_files


def filter_ext(exts=[]):
    """
    Decorator filtering unwanted extensions.
    Returns array of files with wanted extensions.
    Don't use it if you need all files from directory. Use normal function.
    """

    def decorator(function):

        def wrapper(*args, **kwargs):

            files = function(*args, **kwargs)
            return [file for file in files if file.split('.')[-1] in exts]
        
        return wrapper

    return decorator
