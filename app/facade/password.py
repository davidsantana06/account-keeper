from random import choice
from string import ascii_letters as letters, digits, punctuation
from typing import Literal, get_args


class Password:
    Complexity = Literal["low", "medium", "high"]

    __COMPLEXITIES = get_args(Complexity)
    LOW_COMPLEXITY = __COMPLEXITIES[0]
    MEDIUM_COMPLEXITY = __COMPLEXITIES[1]
    HIGH_COMPLEXITY = __COMPLEXITIES[2]

    @classmethod
    def __get_specs(cls, complexity: Complexity) -> tuple[str, int]:
        return {
            cls.LOW_COMPLEXITY: (letters + digits, 12),
            cls.MEDIUM_COMPLEXITY: (letters + digits, 18),
            cls.HIGH_COMPLEXITY: (letters + digits + punctuation, 24),
        }[complexity]

    @classmethod
    def generate(cls, complexity: Complexity) -> str:
        chars, length = cls.__get_specs(complexity)
        choiced_chars = [choice(chars) for _ in range(length)]
        return "".join(choiced_chars)
