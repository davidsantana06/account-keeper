import platform
import webview

from app.config import Parameter

from . import app


def run_in_windows():
    webview.create_window("Account Keeper", app, min_size=(1024, 768))
    webview.start()


def run_in_other_systems():
    app.run(port=Parameter.PORT)


if __name__ == "__main__":
    is_windows = platform.system() == "Windows"
    runner = run_in_windows if is_windows else run_in_other_systems
    runner()
