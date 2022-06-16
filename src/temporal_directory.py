import random
from string import hexdigits
from os import path, makedirs
from shutil import rmtree


def create(basepath: str) -> str:
    """
    Create a temporal folder and return the full directory
    """
    characters = ''.join(random.choice(hexdigits) for i in range(20))
    tmp_directory = path.join(basepath, "static", "documents", characters)
    makedirs(tmp_directory, exist_ok=True)
    return tmp_directory


def remove(tmp_directory) -> None:
    """
    Remove the temporal folder
    """
    if path.isdir(tmp_directory):
        rmtree(tmp_directory)
