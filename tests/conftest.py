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

from smartpasslib.factories import GeneratorsFactory
from smartpasslib.generators import UrandomGen, BasePassGen, HashGen, KeyGen, SmartPassGen, NormalPassGen
from smartpasslib.manager import SmartPassword, SmartPassMan


@pytest.fixture(name='context')
def context():
    key = ('login', 'secret', 'length', 'pub_key', 'normal_pass', 'smart_pass', 'file')
    Info = namedtuple('Info', key)
    login = 'login'
    secret = 'secret'
    length = 15
    pub_key = '15795be051670afec910bc980189a6011f9f184dea4bbbe4e005e4ca89f3' \
              '18bea963b1a362167b4de909a4f57e1895298f79346068487881c8c969dce4fe909f'
    normal_pass = 'urJ77!IK[9?f6|D'
    smart_pass = 'fRIe?Ro9rE6a6fB'
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


@pytest.fixture(name='gen_factory')
def gen_factories():
    return GeneratorsFactory()


@pytest.fixture(name='urandom')
def urandom():
    return UrandomGen()


@pytest.fixture(name='default')
def default():
    return BasePassGen()


@pytest.fixture(name='hash_gen')
def hash_gen():
    return HashGen()


@pytest.fixture(name='key_gen')
def key_gen():
    return KeyGen()


@pytest.fixture(name='smart')
def smart():
    return SmartPassGen()


@pytest.fixture(name='normal')
def normal():
    return NormalPassGen()


@pytest.fixture(name='smart_password')
def smart_password(context):
    return SmartPassword(login=context.login, key=context.pub_key, length=context.length)


@pytest.fixture(name='pass_man')
def pass_man():
    return SmartPassMan()


@pytest.fixture(name='data')
def get_data(context):
    return {
        context.login: {
            'login': context.login,
            'key': context.pub_key,
            'length': context.length
        }
    }


@pytest.fixture(name='file')
def get_file(tmpdir, data):
    a_file = tmpdir.join('new_file')
    with open(a_file, 'w') as f:
        json.dump(data, f)
    yield a_file


@pytest.fixture(name='bad_data')
def get_bad_data(context):
    return {
        context.login: {
            'login': context.login,
            'key': context.pub_key,
            'length': context.length
        },
    }


@pytest.fixture(name='bad_file')
def get_bad_file(file, bad_data):
    file.write(bad_data)
    yield file


@pytest.fixture(name='smart_password2')
def smart_password2(context):
    return SmartPassword(login='login2', key=context.pub_key, length=context.length)
