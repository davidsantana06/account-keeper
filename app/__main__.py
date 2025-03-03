import webview
from . import app


if __name__ == "__main__":
    webview.create_window("Account Keeper", app, min_size=(1024, 768))
    webview.start()
