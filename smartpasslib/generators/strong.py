# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import secrets
import string


class StrongPasswordGenerator:
    """Strong password generator ensuring at least one character from each category."""

    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    digits = string.digits
    symbols = '!@#$%&^_'

    @classmethod
    def generate(cls, length: int = 10) -> str:
        """
        Generates a strong password with guaranteed character diversity.

        Args:
            length (int): Password length (default: 10).

        Returns:
            str: Generated password.

        Raises:
            ValueError: If length is less than 4.
        """
        if length < 4:
            raise ValueError("The length cannot be less than 4.")

        result = [
            secrets.choice(cls.upper_letters),
            secrets.choice(cls.lower_letters),
            secrets.choice(cls.digits),
            secrets.choice(cls.symbols),
        ]
        result += [
            secrets.choice(cls.upper_letters + cls.lower_letters + cls.digits + cls.symbols)
            for _ in range(length - 4)
        ]
        secrets.SystemRandom().shuffle(result)
        return ''.join(result)
