# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
import string
import pytest

from smartpasslib.generators.code import CodeGenerator


class TestBasePasswordGenerator:
    def test_generate_default_length(self):
        password = CodeGenerator.generate(6)
        assert len(password) == 6
        assert any(c in string.ascii_letters for c in password)
        assert any(c in string.digits for c in password)
        assert any(c in CodeGenerator.special_chars for c in password)

    def test_generate_custom_length(self):
        length = 15
        password = CodeGenerator.generate(length=length)
        assert len(password) == length
        assert any(c in string.ascii_letters for c in password)
        assert any(c in string.digits for c in password)
        assert any(c in CodeGenerator.special_chars for c in password)

    def test_generate_minimum_length(self):
        password = CodeGenerator.generate(4)
        assert len(password) == 4
        assert any(c in string.ascii_letters for c in password)
        assert any(c in string.digits for c in password)
        assert any(c in CodeGenerator.special_chars for c in password)

    def test_generate_raises_error_for_short_length(self):
        with pytest.raises(ValueError, match="The code length must be at least 4 characters"):
            CodeGenerator.generate(3)

        with pytest.raises(ValueError, match="The code length must be at least 4 characters"):
            CodeGenerator.generate(0)

        with pytest.raises(ValueError, match="The code length must be at least 4 characters"):
            CodeGenerator.generate(-1)
