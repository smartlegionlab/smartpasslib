# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smartpasslib.generators.smart import SmartPasswordGenerator


class TestSmartPasswordGenerator:
    def test_generate_with_seed(self):
        seed = "test_seed"
        password1 = SmartPasswordGenerator.generate(seed=seed)
        password2 = SmartPasswordGenerator.generate(seed=seed)
        assert password1 == password2

    def test_generate_without_seed(self):
        password1 = SmartPasswordGenerator.generate()
        password2 = SmartPasswordGenerator.generate()
        assert password1 != password2

    def test_get_seed(self):
        seed = SmartPasswordGenerator.get_seed()
        assert isinstance(seed, bytes)
        assert len(seed) == 32