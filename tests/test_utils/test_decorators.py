# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import warnings
from smartpasslib.utils.decorators import deprecated


def test_deprecated_decorator():
    class TestClass:
        def new_method(self):
            return "new"

        @deprecated("new_method")
        def old_method(self):
            return "old"

    with warnings.catch_warnings(record=True) as w:
        obj = TestClass()
        result = obj.old_method()
        assert len(w) == 1
        assert issubclass(w[0].category, DeprecationWarning)
        assert "old_method" in str(w[0].message)
        assert "new_method" in str(w[0].message)
        assert result == "new"
