# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
import pytest

from smartpasslib import SmartPassword
from smartpasslib.managers.smart_password_manager import SmartPasswordManager


class TestSmartPasswordManager:
    def test_add_smart_password(self, temp_file, test_password):
        manager = SmartPasswordManager(filename=temp_file)
        manager.add_smart_password(test_password)
        assert test_password.public_key in manager.smart_passwords

    def test_get_smart_password(self, temp_file, test_password):
        manager = SmartPasswordManager(filename=temp_file)
        manager.add_smart_password(test_password)
        result = manager.get_smart_password(test_password.public_key)
        assert result == test_password

    def test_delete_smart_password(self, temp_file, test_password):
        manager = SmartPasswordManager(filename=temp_file)
        manager.add_smart_password(test_password)
        manager.delete_smart_password(test_password.public_key)
        assert test_password.public_key not in manager.smart_passwords

    def test_clear(self, temp_file, test_password):
        manager = SmartPasswordManager(filename=temp_file)
        manager.add_smart_password(test_password)
        manager.clear()
        assert len(manager.smart_passwords) == 0

    def test_count(self, temp_file, test_password):
        manager = SmartPasswordManager(filename=temp_file)
        manager.add_smart_password(test_password)
        assert manager.password_count == 1

    def test_delete_nonexistent_password(self, temp_file):
        manager = SmartPasswordManager(filename=temp_file)
        with pytest.raises(KeyError, match="Public Key not found."):
            manager.delete_smart_password("nonexistent_key")

    def test_get_nonexistent_password(self, temp_file):
        manager = SmartPasswordManager(filename=temp_file)
        result = manager.get_smart_password("nonexistent_key")
        assert result is None

    def test_passwords_property(self, temp_file, test_password):
        manager = SmartPasswordManager(filename=temp_file)
        manager.add_smart_password(test_password)
        passwords = manager.passwords
        assert isinstance(passwords, dict)
        assert test_password.public_key in passwords
        assert passwords[test_password.public_key] == test_password

    def test_load_data_from_file(self, temp_file, test_password):
        manager1 = SmartPasswordManager(filename=temp_file)
        manager1.add_smart_password(test_password)
        manager2 = SmartPasswordManager(filename=temp_file)
        assert test_password.public_key in manager2.smart_passwords
        assert manager2.password_count == 1

    def test_load_data_from_nonexistent_file(self, tmp_path):
        non_existent_file = tmp_path / "nonexistent.json"
        manager = SmartPasswordManager(filename=str(non_existent_file))
        assert manager.password_count == 0
        assert isinstance(manager.smart_passwords, dict)

    def test_generate_base_password(self):
        password = SmartPasswordManager.generate_base_password()
        assert isinstance(password, str)
        assert len(password) == 12
        password_custom = SmartPasswordManager.generate_base_password(20)
        assert len(password_custom) == 20

    def test_generate_smart_password(self, test_secret):
        password = SmartPasswordManager.generate_smart_password(test_secret)
        assert isinstance(password, str)
        assert len(password) == 12

        password_custom = SmartPasswordManager.generate_smart_password(test_secret, 16)
        assert len(password_custom) == 16

    def test_generate_public_key(self, test_secret):
        public_key = SmartPasswordManager.generate_public_key(test_secret)
        assert isinstance(public_key, str)
        assert len(public_key) > 0

    def test_check_public_key(self, test_secret):
        public_key = SmartPasswordManager.generate_public_key(test_secret)
        assert SmartPasswordManager.check_public_key(test_secret, public_key) is True
        assert SmartPasswordManager.check_public_key("wrong_secret", public_key) is False
        assert SmartPasswordManager.check_public_key(test_secret, "wrong_key") is False

    def test_update_smart_password(self, temp_file, test_password):
        manager = SmartPasswordManager(filename=temp_file)
        manager.add_smart_password(test_password)

        assert manager.update_smart_password(test_password.public_key, description="Updated Description") is True
        updated = manager.get_smart_password(test_password.public_key)
        assert updated.description == "Updated Description"
        assert updated.length == test_password.length  # Length unchanged

        assert manager.update_smart_password(test_password.public_key, length=20) is True
        updated = manager.get_smart_password(test_password.public_key)
        assert updated.description == "Updated Description"  # Description unchanged
        assert updated.length == 20

        assert manager.update_smart_password(
            test_password.public_key,
            description="Final Description",
            length=16
        ) is True
        updated = manager.get_smart_password(test_password.public_key)
        assert updated.description == "Final Description"
        assert updated.length == 16

        manager2 = SmartPasswordManager(filename=temp_file)
        reloaded = manager2.get_smart_password(test_password.public_key)
        assert reloaded.description == "Final Description"
        assert reloaded.length == 16

    def test_update_nonexistent_password(self, temp_file):
        manager = SmartPasswordManager(filename=temp_file)
        assert manager.update_smart_password("nonexistent_key", description="Test") is False

    def test_update_invalid_length(self, temp_file, test_password):
        manager = SmartPasswordManager(filename=temp_file)
        manager.add_smart_password(test_password)

        with pytest.raises(ValueError, match="Password length must be at least 1 character"):
            manager.update_smart_password(test_password.public_key, length=0)

        original = manager.get_smart_password(test_password.public_key)
        assert original.length == test_password.length
        assert original.description == test_password.description

    def test_update_no_changes(self, temp_file, test_password):
        manager = SmartPasswordManager(filename=temp_file)
        manager.add_smart_password(test_password)

        assert manager.update_smart_password(test_password.public_key) is True

        password = manager.get_smart_password(test_password.public_key)
        assert password.description == test_password.description
        assert password.length == test_password.length

    def test_smart_password_update_method(self):
        password = SmartPassword(
            public_key="test_key",
            description="Original Description",
            length=12
        )

        password.update(description="New Description")
        assert password.description == "New Description"
        assert password.length == 12

        password.update(length=20)
        assert password.description == "New Description"
        assert password.length == 20

        password.update(description="Final Description", length=16)
        assert password.description == "Final Description"
        assert password.length == 16

        with pytest.raises(ValueError, match="Password length must be at least 1 character"):
            password.update(length=0)

    def test_smart_password_update_preserves_public_key(self, temp_file, test_password):
        manager = SmartPasswordManager(filename=temp_file)
        manager.add_smart_password(test_password)

        original_public_key = test_password.public_key
        manager.update_smart_password(
            test_password.public_key,
            description="Updated",
            length=20
        )

        updated = manager.get_smart_password(test_password.public_key)
        assert updated.public_key == original_public_key  # Public key unchanged
