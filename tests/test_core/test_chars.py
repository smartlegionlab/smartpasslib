# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import string

from smartpasslib.core.chars import PasswordChars


class TestPasswordChars:
    """Tests for PasswordChars character sets."""

    def test_lowercase(self):
        assert PasswordChars.lowercase == string.ascii_lowercase
        assert len(PasswordChars.lowercase) == 26
        assert all(c.islower() for c in PasswordChars.lowercase)

    def test_uppercase(self):
        assert PasswordChars.uppercase == string.ascii_uppercase
        assert len(PasswordChars.uppercase) == 26
        assert all(c.isupper() for c in PasswordChars.uppercase)

    def test_digits(self):
        assert PasswordChars.digits == string.digits
        assert len(PasswordChars.digits) == 10
        assert all(c.isdigit() for c in PasswordChars.digits)

    def test_symbols(self):
        expected_symbols = '!@#$%^&*()_+-=[]{};:,.<>?/'
        assert PasswordChars.symbols == expected_symbols
        assert len(PasswordChars.symbols) == 26
        assert all(not c.isalnum() for c in PasswordChars.symbols)

    def test_all_method(self):
        expected = PasswordChars.symbols + PasswordChars.uppercase + PasswordChars.digits + PasswordChars.lowercase
        assert PasswordChars.all() == expected
        assert len(PasswordChars.all()) == 52 + 10 + 26
        assert any(c.isalpha() for c in PasswordChars.all())
        assert any(c.isdigit() for c in PasswordChars.all())
        assert any(c in PasswordChars.symbols for c in PasswordChars.all())

    def test_without_symbols_method(self):
        expected = PasswordChars.uppercase + PasswordChars.digits + PasswordChars.lowercase
        assert PasswordChars.without_symbols() == expected
        assert len(PasswordChars.without_symbols()) == 62
        assert all(c.isalnum() for c in PasswordChars.without_symbols())
        assert all(c not in PasswordChars.symbols for c in PasswordChars.without_symbols())

    def test_all_contains_no_duplicates(self):
        all_chars = PasswordChars.all()
        assert len(all_chars) == len(set(all_chars))

    def test_without_symbols_contains_no_duplicates(self):
        chars = PasswordChars.without_symbols()
        assert len(chars) == len(set(chars))

    def test_base_string_consistency(self):
        assert PasswordChars.all() == PasswordChars.BASE_STRING
