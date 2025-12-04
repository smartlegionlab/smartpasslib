# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
from smartpasslib.masters.smart_password_master import SmartPasswordMaster


class TestSmartPasswordMaster:
    def test_generate_base_password(self):
        password = SmartPasswordMaster.generate_base_password()
        assert len(password) == 12

    def test_generate_strong_password(self):
        password = SmartPasswordMaster.generate_strong_password()
        assert len(password) == 12

    def test_generate_smart_password(self, test_secret):
        password = SmartPasswordMaster.generate_smart_password(test_secret)
        assert len(password) == 12

    def test_generate_public_key(self, test_secret):
        pub_key = SmartPasswordMaster.generate_public_key(test_secret)
        assert len(pub_key) == 128

    def test_generate_private_key(self, test_secret):
        private_key = SmartPasswordMaster.generate_private_key(test_secret)
        assert len(private_key) == 128

        private_key2 = SmartPasswordMaster.generate_private_key(test_secret)
        assert private_key == private_key2

        pub_key = SmartPasswordMaster.generate_public_key(test_secret)
        assert private_key == pub_key

    def test_check_public_key(self, test_secret):
        pub_key = SmartPasswordMaster.generate_public_key(test_secret)
        assert SmartPasswordMaster.check_public_key(test_secret, pub_key)

    def test_generate_code(self):
        password = SmartPasswordMaster.generate_code()
        assert len(password) == 8
