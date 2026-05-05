# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
import pytest

from smartpasslib.smart_passwords.smart_password import SmartPassword


class TestSmartPassword:
    def test_init(self, test_description, test_public_key, test_length):
        sp = SmartPassword(public_key=test_public_key, description=test_description, length=test_length)
        assert sp.description == test_description
        assert sp.public_key == test_public_key
        assert sp.length == test_length

    def test_init_default_length(self, test_description, test_public_key):
        sp = SmartPassword(public_key=test_public_key, description=test_description)
        assert sp.length == 12

    def test_init_invalid_length_too_short(self, test_description, test_public_key):
        with pytest.raises(ValueError, match="Password length must be at least 12 characters"):
            SmartPassword(public_key=test_public_key, description=test_description, length=8)

    def test_init_invalid_length_too_long(self, test_description, test_public_key):
        with pytest.raises(ValueError, match="Password length cannot exceed 100 characters"):
            SmartPassword(public_key=test_public_key, description=test_description, length=200)

    def test_update_description(self, test_password):
        test_password.update(description="New Description")
        assert test_password.description == "New Description"
        assert test_password.length == 12

    def test_update_length(self, test_password):
        original_description = test_password.description
        test_password.update(length=20)
        assert test_password.length == 20
        assert test_password.description == original_description

    def test_update_both(self, test_password):
        test_password.update(description="Final", length=16)
        assert test_password.description == "Final"
        assert test_password.length == 16

    def test_update_no_changes(self, test_password):
        original_desc = test_password.description
        original_len = test_password.length
        test_password.update()
        assert test_password.description == original_desc
        assert test_password.length == original_len

    def test_update_invalid_length_too_short(self, test_password):
        with pytest.raises(ValueError, match="Password length must be at least 12 characters"):
            test_password.update(length=8)

    def test_update_invalid_length_too_long(self, test_password):
        with pytest.raises(ValueError, match="Password length cannot exceed 100 characters"):
            test_password.update(length=200)

    def test_to_dict(self, test_password):
        data = test_password.to_dict()
        assert data["public_key"] == test_password.public_key
        assert data["description"] == test_password.description
        assert data["length"] == test_password.length

    def test_from_dict(self, test_password):
        data = test_password.to_dict()
        new_sp = SmartPassword.from_dict(data)
        assert new_sp.public_key == test_password.public_key
        assert new_sp.description == test_password.description
        assert new_sp.length == test_password.length

    def test_properties(self, test_description, test_public_key, test_length):
        sp = SmartPassword(public_key=test_public_key, description=test_description, length=test_length)
        assert sp.public_key == test_public_key
        assert sp.description == test_description
        assert sp.length == test_length
