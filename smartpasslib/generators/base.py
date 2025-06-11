# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import random
import string


class BasePasswordGenerator:
    """Basic password generator with letters, digits, and symbols."""

    letters = string.ascii_letters
    digits = string.digits
    symbols = '!@#$%&^_'

    @classmethod
    def generate(cls, length: int = 10) -> str:
        """
        Generates a password of the specified length.

        Args:
            length (int): Password length (default: 10).

        Returns:
            str: Generated password.
        """
        symbols_string = cls.letters + cls.digits + cls.symbols
        return ''.join((random.choice(symbols_string) for _ in range(length)))
