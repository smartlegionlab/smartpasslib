# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import json
import os
import warnings

from smartpasslib import SmartPasswordMaster


def deprecated(new_method_name):
    def decorator(old_method):
        def wrapper(self, *args, **kwargs):
            warnings.warn(
                f"Method '{old_method.__name__}' is deprecated. Use '{new_method_name}' instead.",
                DeprecationWarning,
                stacklevel=2
            )
            new_method = getattr(self, new_method_name)
            return new_method(*args, **kwargs)
        return wrapper
    return decorator


class SmartPassword:
    def __init__(self, login: str, key: str, length=12):
        self._login = login
        self._length = length
        self._key = key

    @property
    def login(self):
        return self._login

    @property
    def key(self):
        return self._key

    @property
    def length(self):
        return self._length

    def to_dict(self):
        return {
            "login": self._login,
            "key": self._key,
            "length": self._length
        }

    @staticmethod
    def from_dict(data):
        return SmartPassword(login=data['login'], key=data['key'], length=data['length'])


class SmartPasswordFactory:

    @classmethod
    def create_smart_password(cls, login, key, length):
        return SmartPassword(login=login, key=key, length=length)


class SmartPasswordManager:
    def __init__(self, filename='~/.cases.json'):
        self.filename = os.path.expanduser(filename)
        self.smart_passwords = self._load_data()
        self.smart_pass_factory = SmartPasswordFactory()

    @property
    def file_path(self):
        warnings.warn(
            "The 'file_path' attribute is deprecated. Use 'filename' instead.",
            DeprecationWarning,
            stacklevel=2
        )
        return self.filename

    @property
    def passwords(self):
        return self.smart_passwords

    @staticmethod
    def generate_base_password(length=10):
        return SmartPasswordMaster.generate_strong_password(length)

    @classmethod
    def generate_default_smart_password(cls, secret='', length=10):
        return SmartPasswordMaster.generate_default_smart_password(secret, length)

    @classmethod
    def generate_smart_password(cls, login='', secret='', length=10):
        return SmartPasswordMaster.generate_smart_password(login, secret, length)

    @classmethod
    def generate_public_key(cls, login, secret):
        return SmartPasswordMaster.generate_public_key(login, secret)

    @classmethod
    def check_public_key(cls, login, secret, public_key):
        return SmartPasswordMaster.check_public_key(login, secret, public_key)

    @deprecated('add_smart_password')
    def add(self, password):
        self.add_smart_password(password)

    @deprecated('get_smart_password')
    def get_password(self, login: str):
        return self.get_smart_password(login)

    @deprecated('delete_smart_password')
    def remove(self, login: str):
        self.delete_smart_password(login)

    def add_smart_password(self, smart_password: SmartPassword):
        self.smart_passwords[smart_password.login] = smart_password
        self._write_data()

    def get_smart_password(self, login: str):
        return self.smart_passwords.get(login)

    def delete_smart_password(self, login: str):
        if login in self.smart_passwords:
            del self.smart_passwords[login]
            self._write_data()
        else:
            raise KeyError("Login not found.")

    def clear(self):
        self.smart_passwords = {}

    @property
    def count(self):
        return len(self.smart_passwords)

    def _load_data(self):
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return {login: SmartPassword.from_dict(item) for login, item in data.items()}
        else:
            return {}

    def _write_data(self):
        with open(self.filename, 'w') as f:
            json.dump({login: sp.to_dict() for login, sp in self.smart_passwords.items()}, f, indent=4)

    @deprecated('_load_data')
    def load_file(self):
        self._load_data()

    @deprecated('_write_data')
    def save_file(self):
        self._write_data()
