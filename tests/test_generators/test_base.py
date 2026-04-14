# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import string

from smartpasslib.generators.base import BasePasswordGenerator


class TestBasePasswordGenerator:
    """Tests for BasePasswordGenerator."""

    def test_generate_default_length(self):
        """Test generate() with default length (12)."""
        password = BasePasswordGenerator.generate()
        assert len(password) == 12
        # Verify characters are from allowed set
        assert all(c in BasePasswordGenerator.all() for c in password)

    def test_generate_custom_length(self):
        """Test generate() with custom length."""
        length = 15
        password = BasePasswordGenerator.generate(length=length)
        assert len(password) == length
        assert all(c in BasePasswordGenerator.all() for c in password)

    def test_generate_token_default(self):
        """Test generate_token() with default bytes_count (32)."""
        token = BasePasswordGenerator.generate_token()
        assert len(token) == 64  # 32 bytes * 2 = 64 hex chars
        assert all(c in string.hexdigits for c in token)

    def test_generate_token_custom(self):
        """Test generate_token() with custom bytes_count."""
        bytes_count = 16
        token = BasePasswordGenerator.generate_token(bytes_count=bytes_count)
        assert len(token) == bytes_count * 2
        assert all(c in string.hexdigits for c in token)

    def test_generate_urlsafe_token_default(self):
        """Test generate_urlsafe_token() with default bytes_count (32)."""
        token = BasePasswordGenerator.generate_urlsafe_token()
        # URL-safe base64 length: ceil(32*8/6) = 43 characters (approx)
        assert len(token) >= 40
        assert len(token) <= 44
        # No special characters that need escaping in URLs

    def test_generate_urlsafe_token_custom(self):
        """Test generate_urlsafe_token() with custom bytes_count."""
        bytes_count = 16
        token = BasePasswordGenerator.generate_urlsafe_token(bytes_count=bytes_count)
        assert len(token) >= 20
        assert len(token) <= 24
