# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
from smartpasslib.generators.key import SmartKeyGenerator


class TestSmartKeyGenerator:
    def test_generate_public_key(self, test_secret):
        pub_key = SmartKeyGenerator.generate_public_key(test_secret)
        assert isinstance(pub_key, str)
        assert len(pub_key) == 128

    def test_generate_private_key(self, test_secret):
        private_key = SmartKeyGenerator.generate_private_key(test_secret)
        assert len(private_key) == 128

    def test_check_key_valid(self, test_secret):
        public_key = SmartKeyGenerator.generate_public_key(test_secret)
        assert SmartKeyGenerator.check_key(test_secret, public_key)

    def test_check_key_invalid(self, test_secret):
        pub_key = SmartKeyGenerator.generate_public_key(test_secret)
        assert not SmartKeyGenerator.check_key("wrong_secret", pub_key)
