# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smartpasslib import CodeGenerator
from smartpasslib.generators.base import BasePasswordGenerator
from smartpasslib.generators.key import SmartKeyGenerator
from smartpasslib.generators.smart import SmartPasswordGenerator
from smartpasslib.generators.strong import StrongPasswordGenerator


class SmartPasswordMaster:
    """Main class for password and key generation management."""

    @staticmethod
    def generate_code(length: int = 8) -> str:
        return CodeGenerator.generate(length)

    @staticmethod
    def generate_base_password(length: int = 10) -> str:
        """
        Generates a basic password.

        Args:
            length (int): Password length (default: 10).

        Returns:
            str: Generated password.
        """
        return BasePasswordGenerator.generate(length)

    @staticmethod
    def generate_strong_password(length: int = 10) -> str:
        """
        Generates a strong password.

        Args:
            length (int): Password length (default: 10).

        Returns:
            str: Generated password.
        """
        return StrongPasswordGenerator.generate(length)

    @classmethod
    def generate_default_smart_password(cls, secret: str = '', length: int = 10) -> str:
        """
        Generates a smart password using a default method.

        Args:
            secret (str): Secret string.
            length (int): Password length (default: 10).

        Returns:
            str: Generated password.
        """
        return cls.generate_smart_password(secret=secret, length=length)

    @classmethod
    def generate_smart_password(cls, login: str = '', secret: str = '', length: int = 10) -> str:
        """
        Generates a reproducible password based on login and secret.

        Args:
            login (str): User login.
            secret (str): Secret string.
            length (int): Password length (default: 10).

        Returns:
            str: Generated password.
        """
        seed = SmartKeyGenerator.generate_private_key(login, secret)
        return SmartPasswordGenerator.generate(seed, length=length)

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
        return SmartKeyGenerator.generate_public_key(login, secret)

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
        return SmartKeyGenerator.generate_public_key(login, secret)

    @classmethod
    def check_public_key(cls, login: str, secret: str, public_key: str) -> bool:
        """
        Validates a public key against login and secret.

        Args:
            login (str): User login.
            secret (str): Secret string.
            public_key (str): Public key to verify.

        Returns:
            bool: True if the key is valid, False otherwise.
        """
        return SmartKeyGenerator.check_key(login, secret, public_key)
