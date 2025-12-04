# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
from smartpasslib.factories.smart_password_factory import SmartPasswordFactory


class TestSmartPasswordFactory:
    def test_create_smart_password(self, test_public_key, test_description, test_length):
        sp = SmartPasswordFactory.create_smart_password(test_public_key, test_description, test_length)
        assert sp.public_key == test_public_key
        assert sp.description == test_description
        assert sp.length == test_length
