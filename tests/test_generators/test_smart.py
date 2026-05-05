# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import pytest

from smartpasslib.generators.smart import SmartPasswordGenerator


class TestSmartPasswordGenerator:
    def test_generate_default(self, test_secret):
        password = SmartPasswordGenerator.generate(test_secret)
        assert len(password) == 12
        assert all(c in SmartPasswordGenerator.all() for c in password)

    def test_generate_custom_length(self, test_secret):
        password = SmartPasswordGenerator.generate(test_secret, length=20)
        assert len(password) == 20
        assert all(c in SmartPasswordGenerator.all() for c in password)

    def test_generate_deterministic(self, test_secret):
        password1 = SmartPasswordGenerator.generate(test_secret, length=16)
        password2 = SmartPasswordGenerator.generate(test_secret, length=16)
        assert password1 == password2

    def test_generate_different_secrets(self):
        password1 = SmartPasswordGenerator.generate("SecretOne123456", length=16)
        password2 = SmartPasswordGenerator.generate("SecretTwo123456", length=16)
        assert password1 != password2

    def test_generate_different_lengths(self, test_secret):
        password12 = SmartPasswordGenerator.generate(test_secret, length=12)
        password24 = SmartPasswordGenerator.generate(test_secret, length=24)
        assert len(password12) == 12
        assert len(password24) == 24
        assert password12 != password24

    def test_generate_min_length(self, test_secret):
        password = SmartPasswordGenerator.generate(test_secret, length=12)
        assert len(password) == 12

    def test_generate_max_length(self, test_secret):
        password = SmartPasswordGenerator.generate(test_secret, length=100)
        assert len(password) == 100

    def test_generate_invalid_length_too_short(self, test_secret):
        with pytest.raises(ValueError, match="Password length must be at least 12 characters"):
            SmartPasswordGenerator.generate(test_secret, length=8)

    def test_generate_invalid_length_too_long(self, test_secret):
        with pytest.raises(ValueError, match="Password length cannot exceed 100 characters"):
            SmartPasswordGenerator.generate(test_secret, length=200)

    def test_generate_short_secret(self):
        with pytest.raises(ValueError, match="Secret phrase must be at least 12 characters"):
            SmartPasswordGenerator.generate("short", length=16)

    def test_generate_empty_secret(self):
        with pytest.raises(ValueError, match="Secret phrase must be at least 12 characters"):
            SmartPasswordGenerator.generate("", length=16)

    def test_generate_none_secret(self):
        with pytest.raises(ValueError, match="Secret phrase must be at least 12 characters"):
            SmartPasswordGenerator.generate(None, length=16)

    def test_all_characters_used(self, test_secret):
        password = SmartPasswordGenerator.generate(test_secret, length=50)
        for c in password:
            assert c in SmartPasswordGenerator.all()

    def test_cross_platform_compatibility(self):
        secret = "MyCatHippo2026"
        password = SmartPasswordGenerator.generate(secret, length=16)
        expected = "A-UrF0mcpQ:,V2E^"
        assert password == expected

    def test_cross_platform_compatibility_length_12(self):
        secret = "MyCatHippo2026"
        password = SmartPasswordGenerator.generate(secret, length=12)
        expected = "A-UrF0mcpQ:,"
        assert password == expected

    def test_cross_platform_compatibility_another_secret(self):
        secret = "TestSecret2026!"
        password = SmartPasswordGenerator.generate(secret, length=16)
        expected = "ECfA05bxCyi@f&Xb"
        assert password == expected
