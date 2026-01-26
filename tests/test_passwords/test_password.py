# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
from smartpasslib.smart_passwords.smart_password import SmartPassword


class TestSmartPassword:
    def test_init(self, test_description, test_public_key, test_length):
        sp = SmartPassword(description=test_description, public_key=test_public_key, length=test_length)
        assert sp.description == test_description
        assert sp.public_key == test_public_key
        assert sp.length == test_length

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
