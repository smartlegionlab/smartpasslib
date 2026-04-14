# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import hashlib
from smartpasslib.generators.hash import HashGenerator


class TestHashGenerator:
    def test_generate_sha3_256(self):
        test_text = "test_string"
        expected_hash = hashlib.sha256(test_text.encode('utf-8')).hexdigest()
        assert HashGenerator.generate(test_text) == expected_hash

    def test_generate_empty_string(self):
        assert len(HashGenerator.generate("")) == 64
