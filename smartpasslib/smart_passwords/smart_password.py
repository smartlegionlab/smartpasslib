# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from typing import Dict


class SmartPassword:
    """
    Class representing a smart password with associated metadata.

    Attributes:
        _login (str): User login associated with the password.
        _key (str): Key used for password generation.
        _length (int): Length of the generated password.
    """

    def __init__(self, login: str, key: str, length: int = 12):
        """
        Initialize a SmartPassword instance.

        Args:
            login (str): User login.
            key (str): Key used for password generation.
            length (int, optional): Password length. Defaults to 12.
        """
        self._login = login
        self._length = length
        self._key = key

    @property
    def login(self) -> str:
        """str: Get the associated login."""
        return self._login

    @property
    def key(self) -> str:
        """str: Get the generation key."""
        return self._key

    @property
    def length(self) -> int:
        """int: Get the password length."""
        return self._length

    def to_dict(self) -> Dict[str, str | int]:
        """
        Convert the SmartPassword to a dictionary.

        Returns:
            dict: Dictionary representation of the SmartPassword.
        """
        return {
            "login": self._login,
            "key": self._key,
            "length": self._length
        }

    @staticmethod
    def from_dict(data: Dict[str, str | int]) -> 'SmartPassword':
        """
        Create a SmartPassword from a dictionary.

        Args:
            data (dict): Dictionary containing login, key, and length.

        Returns:
            SmartPassword: New SmartPassword instance.
        """
        return SmartPassword(login=data['login'], key=data['key'], length=data['length'])
