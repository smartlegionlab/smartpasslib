# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import string
import pytest

from smartpasslib.generators.strong import StrongPasswordGenerator


class TestStrongPasswordGenerator:
    def test_generate_strong_password(self):
        password = StrongPasswordGenerator.generate()
        assert len(password) == 12
        assert any(c in string.ascii_uppercase for c in password)
        assert any(c in string.ascii_lowercase for c in password)
        assert any(c in string.digits for c in password)
        assert any(c in StrongPasswordGenerator.symbols for c in password)

    def test_generate_custom_length(self):
        password = StrongPasswordGenerator.generate(length=20)
        assert len(password) == 20

    def test_generate_min_length(self):
        password = StrongPasswordGenerator.generate(length=12)
        assert len(password) == 12

    def test_generate_max_length(self):
        password = StrongPasswordGenerator.generate(length=100)
        assert len(password) == 100

    def test_generate_short_length_error(self):
        with pytest.raises(ValueError, match="Password length must be at least 12 characters"):
            StrongPasswordGenerator.generate(length=8)

    def test_generate_long_length_error(self):
        with pytest.raises(ValueError, match="Password length cannot exceed 100 characters"):
            StrongPasswordGenerator.generate(length=200)
