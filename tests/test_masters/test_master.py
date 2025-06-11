# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smartpasslib.masters.smart_password_master import SmartPasswordMaster


class TestSmartPasswordMaster:
    def test_generate_base_password(self):
        password = SmartPasswordMaster.generate_base_password()
        assert len(password) == 10

    def test_generate_strong_password(self):
        password = SmartPasswordMaster.generate_strong_password()
        assert len(password) == 10

    def test_generate_smart_password(self, test_login, test_secret):
        password = SmartPasswordMaster.generate_smart_password(test_login, test_secret)
        assert len(password) == 10

    def test_generate_public_key(self, test_login, test_secret):
        pub_key = SmartPasswordMaster.generate_public_key(test_login, test_secret)
        assert len(pub_key) == 128

    def test_check_public_key(self, test_login, test_secret):
        pub_key = SmartPasswordMaster.generate_public_key(test_login, test_secret)
        assert SmartPasswordMaster.check_public_key(test_login, test_secret, pub_key)

    def test_generate_code(self):
        password = SmartPasswordMaster.generate_code()
        assert len(password) == 8
