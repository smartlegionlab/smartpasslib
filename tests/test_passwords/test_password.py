# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smartpasslib.smart_passwords.smart_password import SmartPassword


class TestSmartPassword:
    def test_init(self, test_login, test_key, test_length):
        sp = SmartPassword(login=test_login, key=test_key, length=test_length)
        assert sp.login == test_login
        assert sp.key == test_key
        assert sp.length == test_length

    def test_to_dict(self, test_password):
        data = test_password.to_dict()
        assert data["login"] == test_password.login
        assert data["key"] == test_password.key
        assert data["length"] == test_password.length

    def test_from_dict(self, test_password):
        data = test_password.to_dict()
        new_sp = SmartPassword.from_dict(data)
        assert new_sp.login == test_password.login
        assert new_sp.key == test_password.key
        assert new_sp.length == test_password.length
