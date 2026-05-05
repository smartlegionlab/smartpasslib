# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import string
import pytest

from smartpasslib.generators.base import BasePasswordGenerator


class TestBasePasswordGenerator:
    """Tests for BasePasswordGenerator."""

    def test_generate_default_length(self):
        password = BasePasswordGenerator.generate()
        assert len(password) == 12
        assert all(c in BasePasswordGenerator.all() for c in password)

    def test_generate_custom_length(self):
        length = 15
        password = BasePasswordGenerator.generate(length=length)
        assert len(password) == length
        assert all(c in BasePasswordGenerator.all() for c in password)

    def test_generate_min_length(self):
        password = BasePasswordGenerator.generate(length=12)
        assert len(password) == 12

    def test_generate_max_length(self):
        password = BasePasswordGenerator.generate(length=100)
        assert len(password) == 100

    def test_generate_invalid_length_too_short(self):
        with pytest.raises(ValueError, match="Password length must be at least 12 characters"):
            BasePasswordGenerator.generate(length=8)

    def test_generate_invalid_length_too_long(self):
        with pytest.raises(ValueError, match="Password length cannot exceed 100 characters"):
            BasePasswordGenerator.generate(length=200)

    def test_generate_token_default(self):
        token = BasePasswordGenerator.generate_token()
        assert len(token) == 64
        assert all(c in string.hexdigits for c in token)

    def test_generate_token_custom(self):
        bytes_count = 16
        token = BasePasswordGenerator.generate_token(bytes_count=bytes_count)
        assert len(token) == bytes_count * 2
        assert all(c in string.hexdigits for c in token)

    def test_generate_urlsafe_token_default(self):
        token = BasePasswordGenerator.generate_urlsafe_token()
        assert len(token) >= 40
        assert len(token) <= 44

    def test_generate_urlsafe_token_custom(self):
        bytes_count = 16
        token = BasePasswordGenerator.generate_urlsafe_token(bytes_count=bytes_count)
        assert len(token) >= 20
        assert len(token) <= 24
