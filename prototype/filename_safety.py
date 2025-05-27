class InvalidFilenameError(Exception):
    pass


def isValidName(filename) -> bool:
    # TODO
    raise NotImplementedError


def validateFilename(filename) -> None:
    if not isValidName(filename):
        raise InvalidFilenameError()
