import webview

from . import app
from .config import Path


if __name__ == "__main__":
    webview.create_window("Account Keeper", app, min_size=(500, 500))
    webview.start(icon=Path.ICON_FILE)
