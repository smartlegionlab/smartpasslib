# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
from smartpasslib.generators.base import BasePasswordGenerator


class TestBasePasswordGenerator:
    def test_generate_default_length(self):
        password = BasePasswordGenerator.generate()
        assert len(password) == 12

    def test_generate_custom_length(self):
        length = 15
        password = BasePasswordGenerator.generate(length=length)
        assert len(password) == length
