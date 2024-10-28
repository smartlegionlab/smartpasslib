# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import json
from pathlib import Path

from smartpasslib import SmartPasswordMaster


class SmartPassword:

    def __init__(self, login='', key='', length=12):
        self._login = login
        self._length = length
        self._key = key

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        self._login = login

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length


class SmartPasswordFactory:

    @classmethod
    def create_smart_password(cls, login, key, length):
        return SmartPassword(login=login, key=key, length=length)


class SmartPasswordManager:
    file_path = Path(Path.home()).joinpath('.cases.json')
    smart_pass_factory = SmartPasswordFactory()

    def __init__(self):
        self._passwords = {}

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
    def check_public_key(cls, login, secret, public_key):
        return SmartPasswordMaster.check_public_key(login, secret, public_key)

    @property
    def passwords(self):
        return self._passwords

    @property
    def count(self):
        return len(self._passwords)

    def add(self, password):
        if password not in self._passwords:
            self._passwords[password.login] = password

    def add_smart_password(self, login, secret, length):
        key = SmartPasswordMaster.generate_public_key(login=login, secret=secret)
        smart_password = self.smart_pass_factory.create_smart_password(
            login=login,
            key=key,
            length=length
        )
        self.add(smart_password)
        return smart_password

    def add_passwords(self, passwords):
        for password in passwords:
            if isinstance(password, SmartPassword):
                self.add(password)

    def get_password(self, login):
        return self._passwords.get(login)

    def remove(self, login: str) -> None:
        if login in self._passwords:
            del self._passwords[login]
        self.save_file()

    def load_file(self):
        try:
            with open(self.file_path, 'r') as f:
                json_data = json.load(f)
        except json.decoder.JSONDecodeError:
            return {}
        except FileNotFoundError:
            self.file_path = Path(Path.home()).joinpath('.cases.json')
            self.save_file()
            return {}
        else:
            passwords = [
                SmartPassword(
                    login=json_data[obj]['login'],
                    key=json_data[obj]['key'],
                    length=max(10, min(json_data[obj]['length'], 1000))
                ) for obj in json_data]
            self.add_passwords(passwords)
            return passwords

    def save_file(self):
        passwords_dict = {name: {'login': password.login,
                                 'length': password.length,
                                 'key': password.key}
                          for name, password in self._passwords.items()}
        self._save_file(passwords_dict)

    def clear(self):
        self._passwords = {}

    def _save_file(self, passwords: dict):
        """Writes json data to a file."""
        with open(self.file_path, 'w') as f:
            json.dump(passwords, f, indent=4)
