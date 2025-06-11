# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smartpasslib.generators.urandom import UrandomGenerator


class TestUrandomGenerator:
    def test_generate_default_size(self):
        result = UrandomGenerator.generate()
        assert isinstance(result, bytes)
        assert len(result) == 32

    def test_generate_custom_size(self):
        size = 64
        result = UrandomGenerator.generate(size=size)
        assert len(result) == size
