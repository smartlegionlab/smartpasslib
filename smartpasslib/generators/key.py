# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smartpasslib.generators.hash import HashGenerator


class SmartKeyGenerator:
    """Key generator based on iterative hashing."""

    @classmethod
    def _create_key(cls, login: str = '', secret: str = '', public_step: int = 15) -> str:
        """
        Internal method for key generation.

        Args:
            login (str): User login.
            secret (str): Secret string.
            public_step (int): Number of hashing iterations.

        Returns:
            str: Generated key.
        """
        login_hash = cls.get_hash(text=login)
        secret_hash = cls.get_hash(text=secret)
        all_hash = cls.get_hash(text=login_hash + secret_hash)
        for _ in range(public_step):
            temp_hash = cls.get_hash(all_hash)
            all_hash = cls.get_hash(all_hash + temp_hash + secret_hash)
        return cls.get_hash(all_hash)

    @classmethod
    def generate_public_key(cls, login: str = '', secret: str = '') -> str:
        """
        Generates a public key.

        Args:
            login (str): User login.
            secret (str): Secret string.

        Returns:
            str: Public key.
        """
        return cls._create_key(login, secret, 60)

    @classmethod
    def generate_private_key(cls, login: str = '', secret: str = '') -> str:
        """
        Generates a private key.

        Args:
            login (str): User login.
            secret (str): Secret string.

        Returns:
            str: Private key.
        """
        return cls._create_key(login, secret, 30)

    @classmethod
    def check_key(cls, login: str = '', secret: str = '', key: str = '') -> bool:
        """
        Verifies if a key matches the given login and secret.

        Args:
            login (str): User login.
            secret (str): Secret string.
            key (str): Key to verify.

        Returns:
            bool: True if the key is valid, False otherwise.
        """
        return cls.generate_public_key(login=login, secret=secret) == key

    @classmethod
    def get_hash(cls, text: str = '') -> str:
        """
        Generates a hash for the given text.

        Args:
            text (str): Input string.

        Returns:
            str: Hash of the input string.
        """
        text = str(text)
        return HashGenerator.generate(str(text.encode('utf-8')))
