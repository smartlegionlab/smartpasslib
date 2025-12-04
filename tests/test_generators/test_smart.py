# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
from smartpasslib.generators.smart import SmartPasswordGenerator


class TestSmartPasswordGenerator:
    def test_generate_with_seed(self):
        seed = "test_seed"
        password1 = SmartPasswordGenerator.generate(seed=seed)
        password2 = SmartPasswordGenerator.generate(seed=seed)
        assert password1 == password2
