# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import warnings
from smartpasslib.managers.smart_password_manager import SmartPasswordManager


class TestSmartPasswordManager:
    def test_add_smart_password(self, temp_file, test_password):
        manager = SmartPasswordManager(filename=temp_file)
        manager.add_smart_password(test_password)
        assert test_password.login in manager.smart_passwords

    def test_get_smart_password(self, temp_file, test_password):
        manager = SmartPasswordManager(filename=temp_file)
        manager.add_smart_password(test_password)
        result = manager.get_smart_password(test_password.login)
        assert result == test_password

    def test_delete_smart_password(self, temp_file, test_password):
        manager = SmartPasswordManager(filename=temp_file)
        manager.add_smart_password(test_password)
        manager.delete_smart_password(test_password.login)
        assert test_password.login not in manager.smart_passwords

    def test_clear(self, temp_file, test_password):
        manager = SmartPasswordManager(filename=temp_file)
        manager.add_smart_password(test_password)
        manager.clear()
        assert len(manager.smart_passwords) == 0

    def test_count(self, temp_file, test_password):
        manager = SmartPasswordManager(filename=temp_file)
        manager.add_smart_password(test_password)
        assert manager.count == 1

    def test_deprecated_methods(self, temp_file, test_password):
        manager = SmartPasswordManager(filename=temp_file)

        with warnings.catch_warnings(record=True) as w:
            manager.add(test_password)
            assert len(w) == 1
            assert issubclass(w[0].category, DeprecationWarning)

        with warnings.catch_warnings(record=True) as w:
            manager.get_password(test_password.login)
            assert len(w) == 1

        with warnings.catch_warnings(record=True) as w:
            manager.remove(test_password.login)
            assert len(w) == 1
