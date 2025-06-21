from platform import system
import webview

from app.config import Parameter

from . import app


def _run_as_window():
    webview.create_window("Account Keeper", app, min_size=(1024, 768))
    webview.start()


def _run_as_server():
    app.run(port=Parameter.PORT)


if __name__ == "__main__":
    is_windows = system() == "Windows"
    runner = _run_as_window if is_windows else _run_as_server
    runner()
