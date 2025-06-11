# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smartpasslib.factories.smart_password_factory import SmartPasswordFactory


class TestSmartPasswordFactory:
    def test_create_smart_password(self, test_login, test_key, test_length):
        sp = SmartPasswordFactory.create_smart_password(test_login, test_key, test_length)
        assert sp.login == test_login
        assert sp.key == test_key
        assert sp.length == test_length
