# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smartpasslib.smart_passwords.smart_password import SmartPassword


class SmartPasswordFactory:
    """Factory class for creating SmartPassword instances."""

    @classmethod
    def create_smart_password(cls, login: str, key: str, length: int) -> SmartPassword:
        """
        Create a new SmartPassword instance.

        Args:
            login (str): User login.
            key (str): Generation key.
            length (int): Password length.

        Returns:
            SmartPassword: New SmartPassword instance.
        """
        return SmartPassword(login=login, key=key, length=length)
