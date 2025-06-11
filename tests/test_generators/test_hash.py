# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import hashlib
from smartpasslib.generators.hash import HashGenerator


class TestHashGenerator:
    def test_generate_sha3_512(self):
        test_text = "test_string"
        expected_hash = hashlib.sha3_512(test_text.encode('utf-8')).hexdigest()
        assert HashGenerator.generate(test_text) == expected_hash

    def test_generate_empty_string(self):
        assert len(HashGenerator.generate("")) == 128
