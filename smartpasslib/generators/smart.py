# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import random
from typing import Union

from smartpasslib.generators.urandom import UrandomGenerator
from smartpasslib.generators.base import BasePasswordGenerator


class SmartPasswordGenerator:
    """Seed-based reproducible password generator."""

    @classmethod
    def generate(cls, seed: Union[str, bytes] = '', length: int = 15, size: int = 32) -> str:
        """
        Generates a password based on a seed.

        Args:
            seed (str | bytes): Seed for reproducibility (if empty, generates a random one).
            length (int): Password length (default: 15).
            size (int): Seed size in bytes (default: 32).

        Returns:
            str: Generated password.
        """
        if not seed:
            seed = cls.get_seed(size)
        cls._set_seed(seed)
        password = BasePasswordGenerator.generate(length)
        seed = str(cls.get_seed())
        cls._set_seed(seed)
        return password

    @classmethod
    def _set_seed(cls, seed: Union[str, bytes]) -> str:
        """
        Sets the random seed for reproducibility.

        Args:
            seed (str | bytes): Seed value.

        Returns:
            str: Seed as a string.
        """
        seed = str(seed)
        random.seed(seed)
        return seed

    @classmethod
    def get_seed(cls, size: int = 32) -> bytes:
        """
        Generates a cryptographically secure random seed.

        Args:
            size (int): Seed size in bytes (default: 32).

        Returns:
            bytes: Random seed.
        """
        return UrandomGenerator.generate(size=size)
