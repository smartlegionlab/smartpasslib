# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import hashlib


class HashGenerator:
    """SHA3-512 hash generator."""

    @classmethod
    def generate(cls, text: str) -> str:
        """
        Generates a SHA3-512 hash for the given text.

        Args:
            text (str): Input string to hash.

        Returns:
            str: Hexadecimal representation of the hash.
        """
        text = str(text)
        sha = hashlib.sha3_512(text.encode('utf-8'))
        return sha.hexdigest()
