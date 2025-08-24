# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
# import string
from smartpasslib.generators.base import BasePasswordGenerator


class TestBasePasswordGenerator:
    def test_generate_default_length(self):
        password = BasePasswordGenerator.generate()
        assert len(password) == 10
        # assert any(c in string.ascii_letters for c in password)
        # assert any(c in string.digits for c in password)
        # assert any(c in BasePasswordGenerator.symbols for c in password)

    def test_generate_custom_length(self):
        length = 15
        password = BasePasswordGenerator.generate(length=length)
        assert len(password) == length
        # assert any(c in string.ascii_letters for c in password)
        # assert any(c in string.digits for c in password)
        # assert any(c in BasePasswordGenerator.symbols for c in password)
