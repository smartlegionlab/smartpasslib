# Copyright (©) 2026, Alexander Suvorov. All rights reserved.
from pathlib import Path

import pytest
import os
from smartpasslib.smart_passwords.smart_password import SmartPassword


@pytest.fixture
def test_description():
    return "test_user"


@pytest.fixture
def test_secret():
    return "secret123"


@pytest.fixture
def test_public_key():
    return "test_public_key"


@pytest.fixture
def test_length():
    return 12


@pytest.fixture
def test_password(test_description, test_public_key, test_length):
    return SmartPassword(description=test_description, public_key=test_public_key, length=test_length)


@pytest.fixture
def temp_file(tmp_path):
    test_file = tmp_path / "test_passwords.json"
    yield str(test_file)
    if os.path.exists(test_file):
        os.remove(test_file)

@pytest.fixture
def mock_home(monkeypatch, tmp_path):
    mock_home_dir = tmp_path / "fake_home"
    mock_home_dir.mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(Path, "home", lambda: mock_home_dir)
    return mock_home_dir
