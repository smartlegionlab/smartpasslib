# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
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
