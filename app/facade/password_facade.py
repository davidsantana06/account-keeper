from random import choice
from string import ascii_letters as letters, digits, punctuation
from typing import Literal, get_args


class PasswordFacade:
    Complexity = Literal["low", "medium", "high"]

    _COMPLEXITIES = get_args(Complexity)
    LOW_COMPLEXITY = _COMPLEXITIES[0]
    MEDIUM_COMPLEXITY = _COMPLEXITIES[1]
    HIGH_COMPLEXITY = _COMPLEXITIES[2]

    @classmethod
    def _get_specs(cls, complexity: Complexity) -> tuple[str, int]:
        return {
            cls.LOW_COMPLEXITY: (letters + digits, 12),
            cls.MEDIUM_COMPLEXITY: (letters + digits, 18),
            cls.HIGH_COMPLEXITY: (letters + digits + punctuation, 24),
        }[complexity]

    @classmethod
    def generate(cls, complexity: Complexity) -> str:
        chars, length = cls._get_specs(complexity)
        return "".join(choice(chars) for _ in range(length))
