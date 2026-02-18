# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import json
from pathlib import Path

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
        with pytest.raises(KeyError, match="Public key not found: nonexistent_key"):
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
        assert updated.length == test_password.length

        assert manager.update_smart_password(test_password.public_key, length=20) is True
        updated = manager.get_smart_password(test_password.public_key)
        assert updated.description == "Updated Description"
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
        assert updated.public_key == original_public_key

    def test_file_path_property(self, temp_file):
        manager = SmartPasswordManager(filename=temp_file)
        assert manager.file_path == temp_file

    def test_generate_base_password_static(self):
        pwd1 = SmartPasswordManager.generate_base_password()
        pwd2 = SmartPasswordManager.generate_base_password(20)
        assert len(pwd1) == 12
        assert len(pwd2) == 20
        assert isinstance(pwd1, str)
        assert isinstance(pwd2, str)

    def test_generate_smart_password_class_method(self, test_secret):
        pwd1 = SmartPasswordManager.generate_smart_password(test_secret)
        pwd2 = SmartPasswordManager.generate_smart_password(test_secret, 20)
        assert len(pwd1) == 12
        assert len(pwd2) == 20
        assert isinstance(pwd1, str)
        assert isinstance(pwd2, str)

    def test_generate_public_key_class_method(self, test_secret):
        key = SmartPasswordManager.generate_public_key(test_secret)
        assert isinstance(key, str)
        assert len(key) > 0

    def test_check_public_key_class_method(self, test_secret):
        key = SmartPasswordManager.generate_public_key(test_secret)
        assert SmartPasswordManager.check_public_key(test_secret, key) is True
        assert SmartPasswordManager.check_public_key("wrong", key) is False

    def test_passwords_property_returns_dict(self, temp_file, test_password):
        manager = SmartPasswordManager(filename=temp_file)
        manager.add_smart_password(test_password)
        assert isinstance(manager.passwords, dict)
        assert len(manager.passwords) == 1

    def test_load_data_corrupted_file(self, temp_file):
        with open(temp_file, 'w') as f:
            f.write("this is not json")

        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            manager = SmartPasswordManager(filename=temp_file)

        assert manager.password_count == 0
        assert isinstance(manager.smart_passwords, dict)

    def test_write_data_permission_error(self, temp_file, monkeypatch, test_password):

        def mock_open(*args, **kwargs):
            raise IOError("Permission denied")

        monkeypatch.setattr("builtins.open", mock_open)

        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            manager = SmartPasswordManager(filename=temp_file)
            manager.add_smart_password(test_password)

        assert test_password.public_key in manager.smart_passwords
        assert manager.get_smart_password(test_password.public_key) == test_password

    def test_default_config_path_creation(self, mock_home):
        manager = SmartPasswordManager()
        expected_path = str(mock_home / '.config' / 'smart_password_manager' / 'passwords.json')
        assert manager.file_path == expected_path
        assert Path(expected_path).parent.exists()

    def test_migration_from_old_file(self, mock_home):
        old_file = mock_home / '.cases.json'
        test_data = {
            "test_key": {
                "public_key": "test_key",
                "description": "test_service",
                "length": 12
            }
        }
        old_file.write_text(json.dumps(test_data))

        manager = SmartPasswordManager()

        new_file = Path(manager.file_path)
        assert new_file.exists()

        assert (mock_home / '.cases.json.bak').exists()
        assert not old_file.exists()

        assert len(manager.smart_passwords) == 1
        assert "test_key" in manager.smart_passwords

    def test_no_migration_if_new_exists(self, mock_home):
        new_file = mock_home / '.config' / 'smart_password_manager' / 'passwords.json'
        new_file.parent.mkdir(parents=True, exist_ok=True)
        new_data = {
            "new_key": {
                "public_key": "new_key",
                "description": "new_service",
                "length": 16
            }
        }
        new_file.write_text(json.dumps(new_data))

        old_file = mock_home / '.cases.json'
        old_file.write_text(json.dumps({"old": "data"}))

        manager = SmartPasswordManager()

        assert len(manager.smart_passwords) == 1
        assert "new_key" in manager.smart_passwords
        assert manager.smart_passwords["new_key"].description == "new_service"

        assert old_file.exists()
        assert not (mock_home / '.cases.json.bak').exists()

    def test_migration_exception_handling(self, mock_home, monkeypatch):
        old_file = mock_home / '.cases.json'
        old_file.touch()

        def mock_copy(*args, **kwargs):
            raise Exception("Mock copy error")

        monkeypatch.setattr("shutil.copy2", mock_copy)

        import io
        import sys
        captured = io.StringIO()
        sys.stderr = captured

        manager = SmartPasswordManager()

        sys.stderr = sys.__stderr__

        assert manager.file_path == str(mock_home / '.config' / 'smart_password_manager' / 'passwords.json')
        assert old_file.exists()

    def test_default_path_with_existing_dir(self, mock_home):
        config_dir = mock_home / '.config' / 'smart_password_manager'
        config_dir.mkdir(parents=True, exist_ok=True)

        manager = SmartPasswordManager()
        assert manager.file_path == str(config_dir / 'passwords.json')
        assert config_dir.exists()