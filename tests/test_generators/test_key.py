# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import pytest

from smartpasslib.generators.key import SmartKeyGenerator


class TestSmartKeyGenerator:
    def test_generate_public_key(self, test_secret):
        pub_key = SmartKeyGenerator.generate_public_key(test_secret)
        assert isinstance(pub_key, str)
        assert len(pub_key) == 64

    def test_generate_public_key_invalid_secret(self):
        with pytest.raises(ValueError, match="Secret phrase must be at least 12 characters"):
            SmartKeyGenerator.generate_public_key("short")

    def test_generate_private_key(self, test_secret):
        private_key = SmartKeyGenerator.generate_private_key(test_secret)
        assert len(private_key) == 64

    def test_generate_private_key_invalid_secret(self):
        with pytest.raises(ValueError, match="Secret phrase must be at least 12 characters"):
            SmartKeyGenerator.generate_private_key("short")

    def test_private_key_different_from_public(self, test_secret):
        private_key = SmartKeyGenerator.generate_private_key(test_secret)
        public_key = SmartKeyGenerator.generate_public_key(test_secret)
        assert private_key != public_key

    def test_check_key_valid(self, test_secret):
        public_key = SmartKeyGenerator.generate_public_key(test_secret)
        assert SmartKeyGenerator.check_key(test_secret, public_key)

    def test_check_key_invalid_secret(self, test_secret):
        public_key = SmartKeyGenerator.generate_public_key(test_secret)
        assert not SmartKeyGenerator.check_key("wrong_secret", public_key)

    def test_check_key_invalid_key(self, test_secret):
        assert not SmartKeyGenerator.check_key(test_secret, "invalid_key")

    def test_check_key_empty_secret(self):
        with pytest.raises(ValueError, match="Secret phrase must be at least 12 characters"):
            SmartKeyGenerator.check_key("", "some_key")

    def test_generate_public_key_deterministic(self, test_secret):
        key1 = SmartKeyGenerator.generate_public_key(test_secret)
        key2 = SmartKeyGenerator.generate_public_key(test_secret)
        assert key1 == key2

    def test_generate_private_key_deterministic(self, test_secret):
        key1 = SmartKeyGenerator.generate_private_key(test_secret)
        key2 = SmartKeyGenerator.generate_private_key(test_secret)
        assert key1 == key2
