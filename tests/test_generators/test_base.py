# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
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
