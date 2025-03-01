from os import path


class Path:
    ROOT_FOLDER = path.abspath(path.dirname(f"{__file__}/../../../.."))
    """ / """

    DATABASE_FILE = path.join(ROOT_FOLDER, "db.sqlite3")
    """ /db.sqlite3 """

    RESOURCE_FOLDER = path.join(ROOT_FOLDER, "resource")
    """ /resource """

    STATIC_FOLDER = path.join(RESOURCE_FOLDER, "static")
    """ /resource/static """

    TEMPLATE_FOLDER = path.join(RESOURCE_FOLDER, "template")
    """ /resource/template """
