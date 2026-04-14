# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import string

from smartpasslib.core.chars import PasswordChars


class TestPasswordChars:
    """Tests for PasswordChars character sets."""

    def test_lowercase(self):
        """Test lowercase letters."""
        assert PasswordChars.lowercase == string.ascii_lowercase
        assert len(PasswordChars.lowercase) == 26
        assert all(c.islower() for c in PasswordChars.lowercase)

    def test_uppercase(self):
        """Test uppercase letters."""
        assert PasswordChars.uppercase == string.ascii_uppercase
        assert len(PasswordChars.uppercase) == 26
        assert all(c.isupper() for c in PasswordChars.uppercase)

    def test_letters(self):
        """Test combined letters (lowercase + uppercase)."""
        assert PasswordChars.letters == string.ascii_letters
        assert len(PasswordChars.letters) == 52
        assert all(c.isalpha() for c in PasswordChars.letters)

    def test_digits(self):
        """Test digits."""
        assert PasswordChars.digits == string.digits
        assert len(PasswordChars.digits) == 10
        assert all(c.isdigit() for c in PasswordChars.digits)

    def test_symbols(self):
        """Test symbols."""
        expected_symbols = '!@#$&*-_'
        assert PasswordChars.symbols == expected_symbols
        assert len(PasswordChars.symbols) == 8
        # Verify no unwanted characters
        assert all(not c.isalnum() for c in PasswordChars.symbols)

    def test_all_method(self):
        """Test all() method returns combined character set."""
        expected = PasswordChars.letters + PasswordChars.digits + PasswordChars.symbols
        assert PasswordChars.all() == expected
        assert len(PasswordChars.all()) == 52 + 10 + 8
        # Verify contains all expected types
        assert any(c.isalpha() for c in PasswordChars.all())
        assert any(c.isdigit() for c in PasswordChars.all())
        assert any(c in PasswordChars.symbols for c in PasswordChars.all())

    def test_without_symbols_method(self):
        """Test without_symbols() method returns letters + digits only."""
        expected = PasswordChars.letters + PasswordChars.digits
        assert PasswordChars.without_symbols() == expected
        assert len(PasswordChars.without_symbols()) == 52 + 10  # 62 characters
        # Verify NO symbols present
        assert all(c.isalnum() for c in PasswordChars.without_symbols())
        assert all(c not in PasswordChars.symbols for c in PasswordChars.without_symbols())

    def test_all_contains_no_duplicates(self):
        """Test that all() has no duplicate characters."""
        all_chars = PasswordChars.all()
        assert len(all_chars) == len(set(all_chars))

    def test_without_symbols_contains_no_duplicates(self):
        """Test that without_symbols() has no duplicate characters."""
        chars = PasswordChars.without_symbols()
        assert len(chars) == len(set(chars))
