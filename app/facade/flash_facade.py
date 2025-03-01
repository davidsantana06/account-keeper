from flask import flash, get_flashed_messages
from typing import Literal


class FlashFacade:
    @staticmethod
    def append(message: str, category: Literal["success", "info"]) -> None:
        flash(message, category)

    @staticmethod
    def pop_all() -> list[tuple[str, str]]:
        flashes = get_flashed_messages(with_categories=True)
        return [(message, category) for category, message in flashes]
