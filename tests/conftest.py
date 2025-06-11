# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import pytest
import os
from smartpasslib.smart_passwords.smart_password import SmartPassword


@pytest.fixture
def test_login():
    return "test_user"


@pytest.fixture
def test_secret():
    return "secret123"


@pytest.fixture
def test_key():
    return "test_key"


@pytest.fixture
def test_length():
    return 12


@pytest.fixture
def test_password(test_login, test_key, test_length):
    return SmartPassword(login=test_login, key=test_key, length=test_length)


@pytest.fixture
def temp_file(tmp_path):
    test_file = tmp_path / "test_passwords.json"
    yield str(test_file)
    if os.path.exists(test_file):
        os.remove(test_file)
