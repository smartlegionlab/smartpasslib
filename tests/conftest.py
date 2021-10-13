# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import json
from collections import namedtuple
from pathlib import Path

import pytest

from smartpasslib import generators
from smartpasslib.managers import PasswordManager
from smartpasslib.passwords import SmartPassword


@pytest.fixture(name='pass_gen')
def pass_gen():
    return generators.PassGen()


@pytest.fixture(name='info')
def get_info():
    key = ('login', 'secret', 'length', 'pub_key', 'normal_pass', 'smart_pass', 'file')
    Info = namedtuple('Info', key)
    login = 'login'
    secret = 'secret'
    length = 15
    pub_key = 'f85e47627d0361b2795f948e52b23c5ca' \
              'f815cb4eb2a4e4ed2c4be3ea9cde6e767' \
              '078dd595a2d0221e33ff42bf7aa3791cd' \
              'cfc3e3161401512b198aa70869ac4'
    normal_pass = 'S3zAp8S{b"NIwi^'
    smart_pass = '@_dH|1F[304lGA3'
    file = Path(Path.home()).joinpath('.cases.json')
    kwargs = dict(
        login=login,
        secret=secret,
        length=length,
        pub_key=pub_key,
        normal_pass=normal_pass,
        smart_pass=smart_pass,
        file=file,
    )
    return Info(**kwargs)


@pytest.fixture(name='hash_login')
def get_hash_text():
    return '63d5cbf2a2135866c520f4' \
           'b47404907891511d1f9a5d' \
           '74e4326befa94120c92e80' \
           '5d6a7ce4e00c8fb0ce607d' \
           '5623b19b5eec17e4b1ce20' \
           'dbdb169cbb07827b9f'


@pytest.fixture(name='hash_gen')
def hash_gen():
    return generators.HashGen()


@pytest.fixture(name='key_gen')
def key_gen():
    return generators.KeyGen()


@pytest.fixture(name='smart_pass_generator')
def smart_pass_generator():
    return generators.SmartPassGen()


@pytest.fixture(name='normal_pass_gen')
def normal_pass_gen():
    return generators.NormalPassGen()


@pytest.fixture(name='gen_factory')
def gen_factory():
    return generators.GeneratorsFactory()


@pytest.fixture(name='passwords_generator')
def passwords_generator():
    return generators.PasswordsGenerator()


@pytest.fixture(name='func_norm_pass_gen')
def func_norm_pass_gen():
    return generators.norm_pass_gen


@pytest.fixture(name='func_smart_pass_gen')
def func_smart_pass_gen():
    return generators.smart_pass_gen


@pytest.fixture(name='func_get_random_data')
def func_get_random_data():
    return generators.get_random_data


@pytest.fixture(name='func_def_pass_gen')
def func_def_pass_gen():
    return generators.def_pass_gen


@pytest.fixture(name='func_get_hash')
def func_get_hash():
    return generators.get_hash


@pytest.fixture(name='func_get_key')
def func_get_key():
    return generators.get_key


@pytest.fixture(name='func_check_key')
def func_check_key():
    return generators.check_key


@pytest.fixture(name='smart_password')
def smart_password(info):
    return SmartPassword(login=info.login, key=info.pub_key, length=info.length)


@pytest.fixture(name='smart_password2')
def smart_password2(info):
    return SmartPassword(login='login2', key=info.pub_key, length=info.length)


@pytest.fixture(name='pass_man')
def pass_man():
    return PasswordManager()


@pytest.fixture(name='data')
def get_data(info):
    return {
        info.login: {
            'login': info.login,
            'key': info.pub_key,
            'length': info.length
        }
    }


@pytest.fixture(name='bad_data')
def get_bad_data(info):
    return {
        info.login: {
            'login': info.login,
            'key': info.pub_key,
            'length': info.length
        },
    }


@pytest.fixture(name='file')
def get_file(tmpdir, data):
    a_file = tmpdir.join('new_file')
    with open(a_file, 'w') as f:
        json.dump(data, f)
    yield a_file


@pytest.fixture(name='bad_file')
def get_bad_file(file, bad_data):
    file.write(bad_data)
    yield file
