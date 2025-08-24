# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
from smartpasslib.generators.key import SmartKeyGenerator


class TestSmartKeyGenerator:
    def test_generate_public_key(self, test_login, test_secret):
        pub_key = SmartKeyGenerator.generate_public_key(test_login, test_secret)
        assert isinstance(pub_key, str)
        assert len(pub_key) == 128

    def test_generate_private_key(self, test_login, test_secret):
        priv_key = SmartKeyGenerator.generate_private_key(test_login, test_secret)
        assert len(priv_key) == 128

    def test_check_key_valid(self, test_login, test_secret):
        pub_key = SmartKeyGenerator.generate_public_key(test_login, test_secret)
        assert SmartKeyGenerator.check_key(test_login, test_secret, pub_key)

    def test_check_key_invalid(self, test_login, test_secret):
        pub_key = SmartKeyGenerator.generate_public_key(test_login, test_secret)
        assert not SmartKeyGenerator.check_key(test_login, "wrong_secret", pub_key)
