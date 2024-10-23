from typing import Literal, get_args
from random import SystemRandom


Level = Literal['weak', 'medium', 'strong']


_LETTERS = 'aAbBcCdDeEfFgGhHijJkKLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
_NUMBERS = '23456789'
_SPECIALS = '#$&-@_~'

LEVELS = get_args(Level)
WEAK = LEVELS[0]
MEDIUM = LEVELS[1]
STRONG = LEVELS[2]

_INFO = {
    WEAK: {'chars': _LETTERS + _NUMBERS, 'length': 12},
    MEDIUM: {
        'chars': _LETTERS + _NUMBERS + _SPECIALS[:3],
        'length': 16
    },
    STRONG: {
        'chars': _LETTERS + _NUMBERS + _SPECIALS,
        'length': 20
    }
}


def _choice_chars(content: str, length: int) -> str:
    random = SystemRandom()
    return ''.join(random.choice(content) for _ in range(length))


def generate(level: Level) -> str:
    info = _INFO[level]
    return _choice_chars(info['chars'], info['length'])
