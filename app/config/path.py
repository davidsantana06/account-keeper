from os import path


class Path:
    ROOT_DIR = path.abspath(path.dirname(f"{__file__}/../../../.."))
    """ / """

    RESOURCE_DIR = path.join(ROOT_DIR, "resource")
    """ /resource """

    STATIC_DIR = path.join(RESOURCE_DIR, "static")
    """ /resource/static """

    TEMPLATE_DIR = path.join(RESOURCE_DIR, "template")
    """ /resource/template """

    STORAGE_DIR = path.join(ROOT_DIR, "storage")
    """ /storage """

    DATABASE_FILE = path.join(STORAGE_DIR, "database.sqlite3")
    """ /storage/database.sqlite3 """
