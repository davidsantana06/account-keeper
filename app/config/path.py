from os import path


class Path:
    ROOT_DIR = path.abspath(path.dirname(f"{__file__}/../../../.."))
    """ / """

    DATABASE_FILE = path.join(ROOT_DIR, "database.sqlite3")
    """ /database.sqlite3 """

    RESOURCE_DIR = path.join(ROOT_DIR, "resource")
    """ /resource """

    STATIC_DIR = path.join(RESOURCE_DIR, "static")
    """ /resource/static """

    ICON_FILE = path.join(STATIC_DIR, "img", "i-logo-dark.png")
    """ /resource/static/img/b-logo-dark.png """

    TEMPLATE_DIR = path.join(RESOURCE_DIR, "template")
    """ /resource/template """
