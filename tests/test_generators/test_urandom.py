# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import pytest

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

    def test_generate_min_size(self):
        result = UrandomGenerator.generate(size=1)
        assert len(result) == 1

    def test_generate_max_size(self):
        result = UrandomGenerator.generate(size=1024 * 1024)
        assert len(result) == 1024 * 1024

    def test_generate_invalid_size_too_small(self):
        with pytest.raises(ValueError, match="Size must be at least 1 byte"):
            UrandomGenerator.generate(size=0)

    def test_generate_invalid_size_negative(self):
        with pytest.raises(ValueError, match="Size must be at least 1 byte"):
            UrandomGenerator.generate(size=-5)

    def test_generate_invalid_size_too_large(self):
        with pytest.raises(ValueError, match="Size cannot exceed 1 MB"):
            UrandomGenerator.generate(size=1024 * 1024 + 1)
