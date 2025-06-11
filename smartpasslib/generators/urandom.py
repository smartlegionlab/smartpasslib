# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import os


class UrandomGenerator:
    """Cryptographically secure random bytes generator using `os.urandom`."""

    @classmethod
    def generate(cls, size: int = 32) -> bytes:
        """
        Generates random bytes of the specified size.

        Args:
            size (int): Number of bytes to generate (default: 32).

        Returns:
            bytes: Random byte string.
        """
        return os.urandom(size)
