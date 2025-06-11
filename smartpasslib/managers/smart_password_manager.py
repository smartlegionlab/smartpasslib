# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import json
import os
import warnings
from typing import Dict, Optional

from smartpasslib.masters.smart_password_master import SmartPasswordMaster
from smartpasslib.factories.smart_password_factory import SmartPasswordFactory
from smartpasslib.smart_passwords.smart_password import SmartPassword
from smartpasslib.utils.decorators import deprecated


class SmartPasswordManager:
    """
    Manager class for storing and retrieving SmartPassword instances.

    Attributes:
        filename (str): Path to the storage file.
        smart_passwords (dict): Dictionary of stored passwords.
        smart_pass_factory (SmartPasswordFactory): Factory for password creation.
    """

    def __init__(self, filename: str = '~/.cases.json'):
        """
        Initialize the SmartPasswordManager.

        Args:
            filename (str, optional): Path to storage file. Defaults to '~/.cases.json'.
        """
        self.filename = os.path.expanduser(filename)
        self.smart_passwords = self._load_data()
        self.smart_pass_factory = SmartPasswordFactory()

    @property
    def file_path(self) -> str:
        """
        str: Deprecated property for filename (use filename instead).

        Returns:
            str: The filename path.

        Warns:
            DeprecationWarning: Indicates this property is deprecated.
        """
        warnings.warn(
            "The 'file_path' attribute is deprecated. Use 'filename' instead.",
            DeprecationWarning,
            stacklevel=2
        )
        return self.filename

    @property
    def passwords(self) -> Dict[str, SmartPassword]:
        """dict: Get all stored smart passwords."""
        return self.smart_passwords

    @staticmethod
    def generate_base_password(length: int = 10) -> str:
        """
        Generate a base password.

        Args:
            length (int, optional): Password length. Defaults to 10.

        Returns:
            str: Generated password.
        """
        return SmartPasswordMaster.generate_strong_password(length)

    @classmethod
    def generate_default_smart_password(cls, secret: str = '', length: int = 10) -> str:
        """
        Generate a default smart password.

        Args:
            secret (str, optional): Secret for generation. Defaults to ''.
            length (int, optional): Password length. Defaults to 10.

        Returns:
            str: Generated password.
        """
        return SmartPasswordMaster.generate_default_smart_password(secret, length)

    @classmethod
    def generate_smart_password(cls, login: str = '', secret: str = '', length: int = 10) -> str:
        """
        Generate a smart password.

        Args:
            login (str, optional): User login. Defaults to ''.
            secret (str, optional): Secret for generation. Defaults to ''.
            length (int, optional): Password length. Defaults to 10.

        Returns:
            str: Generated password.
        """
        return SmartPasswordMaster.generate_smart_password(login, secret, length)

    @classmethod
    def generate_public_key(cls, login: str, secret: str) -> str:
        """
        Generate a public key.

        Args:
            login (str): User login.
            secret (str): Secret for generation.

        Returns:
            str: Generated public key.
        """
        return SmartPasswordMaster.generate_public_key(login, secret)

    @classmethod
    def check_public_key(cls, login: str, secret: str, public_key: str) -> bool:
        """
        Verify a public key.

        Args:
            login (str): User login.
            secret (str): Secret for verification.
            public_key (str): Key to verify.

        Returns:
            bool: True if the key is valid, False otherwise.
        """
        return SmartPasswordMaster.check_public_key(login, secret, public_key)

    @deprecated('add_smart_password')
    def add(self, password: SmartPassword):
        """Deprecated method for adding a password."""
        self.add_smart_password(password)

    @deprecated('get_smart_password')
    def get_password(self, login: str) -> Optional[SmartPassword]:
        """Deprecated method for getting a password."""
        return self.get_smart_password(login)

    @deprecated('delete_smart_password')
    def remove(self, login: str):
        """Deprecated method for removing a password."""
        self.delete_smart_password(login)

    def add_smart_password(self, smart_password: SmartPassword):
        """
        Add a smart password to storage.

        Args:
            smart_password (SmartPassword): Password to add.
        """
        self.smart_passwords[smart_password.login] = smart_password
        self._write_data()

    def get_smart_password(self, login: str) -> Optional[SmartPassword]:
        """
        Get a smart password by login.

        Args:
            login (str): Login to look up.

        Returns:
            SmartPassword or None: The found password or None if not found.
        """
        return self.smart_passwords.get(login)

    def delete_smart_password(self, login: str):
        """
        Delete a smart password by login.

        Args:
            login (str): Login of password to delete.

        Raises:
            KeyError: If login is not found.
        """
        if login in self.smart_passwords:
            del self.smart_passwords[login]
            self._write_data()
        else:
            raise KeyError("Login not found.")

    def clear(self):
        """Clear all stored passwords."""
        self.smart_passwords = {}

    @property
    def count(self) -> int:
        """int: Get the count of stored passwords."""
        return len(self.smart_passwords)

    def _load_data(self) -> Dict[str, SmartPassword]:
        """
        Load password data from file.

        Returns:
            dict: Dictionary of loaded passwords.
        """
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return {login: SmartPassword.from_dict(item) for login, item in data.items()}
        else:
            return {}

    def _write_data(self):
        """Write password data to file."""
        with open(self.filename, 'w') as f:
            json.dump({login: sp.to_dict() for login, sp in self.smart_passwords.items()}, f, indent=4)

    @deprecated('_load_data')
    def load_file(self):
        """Deprecated method for loading data."""
        self._load_data()

    @deprecated('_write_data')
    def save_file(self):
        """Deprecated method for saving data."""
        self._write_data()
