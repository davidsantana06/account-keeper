from os import path


class Path:
    ROOT_FOLDER = path.abspath(path.dirname(f"{__file__}/../../../.."))
    """ / """

    ENV_FILE = path.join(ROOT_FOLDER, ".env")
    """ .env """

    DATABASE_FILE = path.join(ROOT_FOLDER, "db.sqlite3")
    """ /db.sqlite3 """

    STATIC_FOLDER = path.join(ROOT_FOLDER, "static")
    """ /static/ """

    TEMPLATE_FOLDER = path.join(ROOT_FOLDER, "template")
    """ /template/ """
