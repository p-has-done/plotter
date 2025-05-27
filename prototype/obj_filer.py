from pickle import dump, load
from filename_safety import validateFilename


def dumpObj(obj, filename):
    validateFilename(filename)
    with open(filename, "wb") as file:
        dump(obj, file)


def loadObj(obj, filename):
    validateFilename(filename)
    with open(filename, "rb") as file:
        return load(obj, file)
