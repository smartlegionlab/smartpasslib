# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import string
import pytest
from smartpasslib.generators.strong import StrongPasswordGenerator


class TestStrongPasswordGenerator:
    def test_generate_strong_password(self):
        password = StrongPasswordGenerator.generate()
        assert len(password) == 10
        assert any(c in string.ascii_uppercase for c in password)
        assert any(c in string.ascii_lowercase for c in password)
        assert any(c in string.digits for c in password)
        assert any(c in StrongPasswordGenerator.symbols for c in password)

    def test_generate_short_length_error(self):
        with pytest.raises(ValueError):
            StrongPasswordGenerator.generate(length=3)
